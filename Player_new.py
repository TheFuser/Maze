import numpy as np
from PIL import Image
class Player:
    def __init__(self)-> None:
        self.pos=np.array([0, 0])
        self.dir=np.array([15, 6])
        self.cam_size = 100, 40
        self.render_distance=10
        self.cam_focal_distance=.2
        self.screen_scale=1

    def print_infos(self):
        print('='*10+' PLAYER INFOS '+ '='*10)
        print(f'Position {self.pos}')
        print(f'dir {self.dir}')
        print(f'CAMERA INFOS')
        print()
        
        print(f'cam_size {self.cam_size}')
        print(f'render_distance {self.render_distance}')
        print(f'cam_focal_distance {self.cam_focal_distance}')
        print(f'screen_scale {self.screen_scale}')
    def rotate(self, theta):
        if (0, 0) in self.dir:
            return
        x, y=self.dir
        if x==0:
            self.dir=np.array([np.sin(theta),np.cos(theta)])
            
        alpha=np.arctan(y/x)
        self.dir=np.array([np.sin(alpha+theta),np.cos(alpha+theta)])

    def set_dir_from_angle(self, theta):
        self.dir= np.cos(theta),np. sin(theta)
        self.dir=np.array(self.dir)

    def generate_image(self, walls):
        background_col=(0, 0, 0)        
        wall_col=(255, 255, 255)
        w, h = self.cam_size
        render_image=[[0 for i in range(w)] for j in range(h)]#TODO : faire avec np
        assert (w, h)==(len(render_image[0]), len(render_image))
        c=0
        colors=[]
        
        for i in range(w):
            #on va faire du raytracing
            dist=10000000
            for wall in walls:
                #Init
                col=0
                
                a=np.array
                sq=lambda x:np.dot(x, x)
                orth=lambda s:a([-s[1], s[0]])
                norm=lambda x:((x[0])**2+(x[1])**2)**.5
                angle_between = lambda a, b : np.arccos(np.dot(a, b)/(norm(a)*norm(b)))

                #Computing
                A, B = wall[0], wall[1]                    
                s=self.cam_focal_distance
                d=a(self.dir)
                d_=orth(d)
                P=a(self.pos)
                d=d/norm(d)
                d_=d_/norm(d_)

                K=P+s*d+d_*(i-w/2)*self.screen_scale/w
                #print(f'A, P, K : {A, P, K }')
                assert sq(K)==sq(K)
                if sq(A-P)==0:
                    colors.append(wall_col)
                    continue
                papk, abpk=angle_between(A-P, K-P),angle_between(B-A, K-P)
                #print(f'papk, abpk: {papk, abpk}')
                if np.sin(abpk)==0:
                    colors.append(background_col)
                    continue
                assert papk==papk and abpk==abpk, (papk, abpk)
                AI = (B-A)*norm(P-A)*np.sin(papk)/np.sin(abpk)/norm(B-A)
                I = A+AI
                assert sq(AI)==sq(AI)
                if sq(A==P) == 2:
                    print(f'A in P : {A} in {P}')
                    c+=1
                    colors.append(wall_col)
                    continue

                #print(f'AI: {AI}')
                #print(f'I: {I}')
                dist=norm(I-P) #norm(I-K) ???
                if dist>self.render_distance:
                    colors.append(background_col)
                    continue
                col = 255*(1-dist/self.render_distance)
                assert 0<=col<=255, f'col : {col,I, P,AI}'
                hm=2
                if type(col)!=int: col=int(col)
                colors.append(col)

                assert len(colors)==self.cam_size[0],f'{len(colors), self.cam_size}'


        print(f"C {c}, {c/w/h}") 
    
        return render_image

    def test(self):
        img = Image.fromarray(self.generate_image())
        img.show()

if __name__=='__main__':
    print('Hi')