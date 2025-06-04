adrs_counter = 0x1
p = 0xB640000002A3A6F1D603AB4FF58EC74521F2934B1A7AEEDBE56F9B27E351457D
# p=17
m = 0
ma = 0
ad = 0
s = 0
n = 0
R = 2**256

Note = open('1.txt', mode='w')


class Fp:


        def __init__(self, v0):
            global adrs_counter
            self.adrs = adrs_counter
            # print("%d\n%d\n"%(v0, v1))
            self.a = v0
            adrs_counter += 1

        def __add__(self, other):
            global ad
            a = self.a
            b = other.a
            c = a + b % p 

            c = Fp(c)
            print('add %05x %05x %05x %d' % (c.adrs, self.adrs, other.adrs, ad))
            Note.write('add %05d %05d %05d %d\n' % (c.adrs, self.adrs, other.adrs, ad))  # \n 换行符
            ad += 1
            # print("c0=%x,\nc1=%x\n"%(c0,c1))
            return c
        ''' 
        def addi(self, other):
            # 自定义加法，不触发统计
            a = self.a
            b = other.a
            c = a + b
            c = Fp(c)
            #print('addi (no count) %05x %05x %05x' % (c.adrs, self.adrs, other.adrs))
            return c
        '''
        def __sub__(self, other):
            global s
            a = self.a
            b = other.a
            c = (a - b) % p
            c = Fp(c)
            print('sub %05x %05x %05x %d' % (c.adrs, self.adrs, other.adrs, s))
            Note.write('sub %05d %05d %05d %d\n' % (c.adrs, self.adrs, other.adrs, s))
            s += 1
            return c
        
        def __mul__(self, other):
            global m
            if isinstance(other, Fp):
                a = self.a
                b = other.a
                c = a * b 
                c = Fp(c)

                print('mul %05x %05x %05x %d' % (c.adrs, self.adrs, other.adrs, m))
                Note.write('mul %05d %05d %05d %d\n' % (c.adrs, self.adrs, other.adrs, m))
                m += 1
                # print("%x\n%x"%(c0,c1))
                return c
            raise TypeError(f"Unsupported operand type(s) for *: 'Fp' and '{type(other).__name__}'")
        
 
            
        '''
        def __mul_add__(self, other, addend):
            global ma
            a = self.a
            b = other.a
            c = addend.a

            # 计算 a * b + c，并取模 p
            d = a * b + c
            d = Fp(d)

            # 记录操作
            print('mul_add %05x %05x %05x %05x %d' % (d.adrs, self.adrs, other.adrs, addend.adrs, m))
            Note.write('mul_add %05d %05d %05d %05d %d\n' % (d.adrs, self.adrs, other.adrs, addend.adrs, m))
            ma += 1
            return d
        
        def __mul_and__(self, other, addend):
            global m
            a = self.a
            b = other.a
            c = addend.a

            # 计算 a * b + c，并取模 p
            d = a * b  % c
            d = Fp(d)

            # 记录操作
            print('mul_add %05x %05x %05x %05x %d' % (d.adrs, self.adrs, other.adrs, addend.adrs, m))
            Note.write('mul_add %05d %05d %05d %05d %d\n' % (d.adrs, self.adrs, other.adrs, addend.adrs, m))
            m += 1
            return d
        '''
        def __mod__(self, other):
            if isinstance(other, int):  # 如果与 int 进行模运算
                return Fp(self.a % other)
            raise TypeError(f"Unsupported operand type(s) for %: 'Fp' and '{type(other).__name__}'")

        def __and__(self, other):
            if isinstance(other, int):  # 如果与 int 类型操作
                return self.a & other
            raise TypeError(f"Unsupported operand type(s) for &: 'Fp' and '{type(other).__name__}'")
        
        def __rshift__(self, other):  # 右移操作符重载
            if isinstance(other, int):
                return self.a >> other
            raise TypeError(f"Unsupported operand type(s) for >>: 'Fp' and '{type(other).__name__}'")

            
        def __lshift__(self, other):  # 左移操作符重载
            if isinstance(other, int):
                return self.a << other
            raise TypeError(f"Unsupported operand type(s) for <<: 'Fp' and '{type(other).__name__}'")
         
        
        def __neg__(self):

            a = self.a
            c = (-a) % p
            c = Fp(c)

            return c
        def inv(self):

            k = self.a
            if k == 0:
                raise ZeroDivisionError('division by zero')

            if k < 0:
                # k ** -1 = p - (-k) ** -1  (mod p)
                return p - inverse_mod(-k, p)

            # Extended Euclidean algorithm.
            s, old_s = 0, 1
            t, old_t = 1, 0
            r, old_r = p, k

            while r != 0:
                quotient = old_r // r
                old_r, r = r, old_r - quotient * r
                old_s, s = s, old_s - quotient * s
                old_t, t = t, old_t - quotient * t

            gcd, x, y = old_r, old_s, old_t

            assert gcd == 1
            assert (k * x) % p == 1
            c=Fp(x % p)
            print('inv %05x %05x 0' % (c.adrs, self.adrs))
            Note.write('inv %05d %05d 0\n' % (c.adrs, self.adrs))
            return c

        def str(self): return "str=Fp2(%x)" % (self.a)

        def czy(self): return self.a

        def yiwei(self):
            #a = self.a
            a = self.a >> 1
            a = Fp(a)
            return a


def inverse_mod(k, p):

    k = Fp.czy(k)
    if k == 0:
        raise ZeroDivisionError('division by zero')

    if k < 0:
        # k ** -1 = p - (-k) ** -1  (mod p)
        return p - inverse_mod(-k, p)

    # Extended Euclidean algorithm.
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = p, k

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    gcd, x, y = old_r, old_s, old_t

    assert gcd == 1
    assert (k * x) % p == 1

    return Fp(x % p)







def r128_mon_mul(a, b, w=128):
    # 初始化 m
    global m

    a0 = Fp(a & ((1 << w) - 1))
    a1 = Fp(a >> w)
    b0 = Fp(b & ((1 << w) - 1))
    b1 = Fp(b >> w)

    p0 = Fp(p & ((1 << w) - 1))
    p1 = Fp(p >> w)
 
    m_prime_int = pow(-p0.a, -1, 1 << w)
    m_prime = Fp(m_prime_int)

    # 初始化 z0 和 z1 为 Fp 类型
    z0 = Fp(0)
    z1 = Fp(0)

    # 第一步：计算 q0 和 c0
    t1 = (a0 * b0) #+ z0           
    q0 = (t1 * m_prime) % (1 << w)  
    c0 = (q0 * p0) #+ t1           
    t2 = (a0 * b1) #+ z1 
    t3 = Fp(c0 >> w)
    c1 = (q0 * p1)  # + t2 + t3  

    # 更新 z0 和 z1
    z0 = Fp(c1.a & ((1 << w) - 1))
    z1 = Fp(c1.a >> w)

    t1 = (a1 * b0)      #+ z0     
    q1 = (t1 * m_prime) % (1 << w)  
    c0 = (q1 * p0) #+ t1             

    # 计算 c1
    t2 = (a1 * b1) # + z1
    t3 = Fp(c0 >> w)
    c1 = (q1 * p1) #+ t2 + t3

    z0 = Fp(c1 & ((1 << w) - 1))
    z1 = Fp(c1 >> w)


    
    S = (z1.a << w) | z0.a   

    z0 = Fp(c1.a & ((1 << w) - 1))
    z1 = Fp(c1.a >> w)

    S = (z1.a << w) | z0.a
    print()
    if S >= p:
        S -= p

    s = Fp(S)
    print('mul %05x %05x %05x %d' % (s.adrs, a.adrs, b.adrs, m))
    Note.write('mul %05d %05d %05d %d\n' % (s.adrs, a.adrs, b.adrs, m))
    return s  
    



'''
def r128_mon_mul(a, b, w=128):

        m = 0xB640000002A3A6F1D603AB4FF58EC74521F2934B1A7AEEDBE56F9B27E351457D
        a0 = Fp(a & ((1 << w) - 1)) 
        a1 = Fp(a >> w)
        b0 = Fp(b & ((1 << w) - 1))
        b1 = Fp(b >> w)

        m0 = Fp(m & ((1 << w) - 1))
        m1 = Fp(m >> w)
        
        m_prime = pow(-m0.a, -1, 1 << w)
        m_p = Fp(m_prime)

        z0 = Fp(0)
        z1 = Fp(0)
        #first round
        t1 = Fp(a0 * b0 + z0)
        t2 = Fp(1 << w)
        q0 = Fp(t1 * m_p % t2)
        c0 = q0 * m0 + t1
        t1 = a0 * b1 + z1
        t3 = Fp(c0 >> w)
        t4 = t1 + t3
        c1 = q0 * m1 + t4
        z0 = c1 & ((1 << w) - 1)
        z1 = c1 >> w
        #second round
        t1 = a1 * b0 + z0
        t2 = 1 << w
        q1 = t1 * m_p % t2
        c0 = q1 * m0 + t1 
        t1 = a1 * b1 + z1
        t3 = c0 >> w
        t4 = t1 + t3
        c1 = q1 * m1 + t4
        z0 = c1 & ((1 << w) - 1)
        z1 = c1 >> w
        #result
        S = z1 << w | z0 
        if S >= m:
            S -= m

        return S
    '''



def fp2_add(a0, a1, b0, b1):
    c0 = a0 + b0
    c1 = a1 + b1

    return c0, c1


def fp2_sub(a0, a1, b0, b1):
    c0 = a0 - b0
    c1 = a1 - b1
    return c0, c1

def fp2_mult(a0, a1, b0, b1):
    
    c0 = r128_mon_mul(a0 , b0)
    
    
    c1 = r128_mon_mul(a1 , b1)
    t0 = a0 + a1
    
    t1 = b0 + b1

    c2 = r128_mon_mul(t0 , t1)
    t0 = c0 + c1

    t1 = c1 + c1

    t0 = c2 - t0
    t1 = c0 - t1
    #print("%x\n%x"%(Fp.czy(c0),Fp.czy(c1)))
    return t1, t0

'''
#test_fp2_mult
a0=0x20bfe66249e3c41774ebe056a2a3449a28b7ddc7fa86683063e3775fbd832398
a1=0x8a97049ad793388f31e5f4e02a200c7246ba07023ef11e9cf9e3978db3dcd80b
c0=0x1ac639962eee863621d77d6c9c715a500bdd4184ebfb4b4bd82a3b40912808dc
c1=0x5cee78c918c29ace3b0315009bd83d7e2d12a487432d929f8b8b66c8f9d7449e
c0, c1 = fp2_mul(a0, a1, c0, c1)
c0 = Fp.czy(c0)
c1 = Fp.czy(c1)
print("c0=%x\nc1=%x" %(c0,c1))
'''
def lode_fp2_inv(a0, a1):
    a0, a1 = Fp(a0), Fp(a1)
    o = Fp(0)
    return a0, a1, o
def fp2_inv(a0, a1):
    c0 = a0*a0
    c1 = a1*a1
    t0 = c1+c1
    t1 = c0+t0
    t0 = o-a1
    r = Fp.inv(t1)
    c0 = r*a0
    c1 = r*t0
    return c0, c1
'''
#test_fp2_inv
a0=0xa11f46eace8662f387e04b03a47084b6d9b56169bf5105b8032e324dd28af0c0
a1=0x23593b79222ea0d36adada78e0fcded533bc34705b4c28fcd93fd6d3110dbf38
c0=0x5a6cba8949d49f50bab871ea8879056fa190aec2f21c7f063a99f8b947baf436
c1=0x81f4d9d702cddc16cce9d6b62aa3a3b21e1f1648d1312c0903a5e2ce97854670
a0, a1, o = lode_fp2_inv(a0, a1)
c00, c01 = fp2_inv(a0, a1)
print("%x\n%x\n"%(Fp.czy(c00), Fp.czy(c01)))
'''
##################################fp4 #######################################
def fp4_add(a00, a01, a10, a11, b00, b01, b10, b11):

    c00, c01 = fp2_add(a00, a01, b00, b01)
    c10, c11 = fp2_add(a10, a11, b10, b11)

    return c00, c01, c10, c11


# (a00+a01u)+(a10+a11u)v   -   (b00+b01u)+(b10+b11u)v   =(c00+c01u)+(c10+c11u)v
def fp4_sub(a00, a01, a10, a11, b00, b01, b10, b11):
    c00, c01 = fp2_sub(a00, a01, b00, b01)
    c10, c11 = fp2_sub(a10, a11, b10, b11)
    return c00, c01, c10, c11


def lode_fp4_mult(a00, a01, a10, a11, b00, b01, b10, b11):
    a0_0 = Fp(a00)
    a0_1 =  Fp(a01)
    a1_0= Fp(a10)
    a1_1 = Fp(a11)
    b0_0= Fp(b00)
    b0_1 = Fp(b01)
    b1_0= Fp(b10)
    b1_1 = Fp(b11)
    o = Fp(0)
    i = Fp(1)
    return a0_0, a0_1, a1_0, a1_1, b0_0, b0_1, b1_0, b1_1, o, i


def fp4_mult(a00, a01, a10, a11, b00, b01, b10, b11):
    """by old"""
    t00, t01 = fp2_mult(a00, a01, b00, b01)  # a0b0
    print("t00=%X,\nt01=%X" % (Fp.czy(t00), Fp.czy(t01)))
    t10, t11 = fp2_mult(a10, a11, b10, b11)  # a1b1
    m00, m01 = fp2_add(a00, a01, a10, a11)  # a0+a1
    m10, m11 = fp2_add(b00, b01, b10, b11)  # b0+b1

    t30, t31 = fp2_sub(o, t10, t11, o)
    t30, t31 = fp2_sub(t30, t31, t11, o)
    t20, t21 = fp2_mult(m00, m01, m10, m11)  # a0+a1 * b0+b1
    c10, c11 = fp2_sub(t20, t21, t00, t01)
    c10, c11 = fp2_sub(c10, c11, t10, t11)

    c00, c01 = fp2_add(t00, t01, t30, t31)

    return c00, c01, c10, c11

'''
#test_fp4_mult
a01  = 0x3CA03C51E4BD5B2952F7975DC4BA732591E225079160F3F67DCFA6F6840EC095
a00  = 0x5CECBFE01B025D57CC41A9AF3258D8FF29AFA7965969BF36D3BE9698E99C6EED
a11  = 0x2339B6764008293F648DEE90C9474E0868F1071F49E95B00757C6FF591A218F8
a10  = 0x79288FB51D662524BE7FA9E092CFCEE028E78E6B6132C1F8017DC791E0A3496F
c00=0x9F594F9C78FC3107C89B5721ACB00E66A73A4C873B92E52D34E857237187B8B1
c01=0x2094882EFA2DCE9052FB94C2B4058109F73149B36B35AB05FFB600F6444AB500
c10=0x5784CD0E3655F30C46FD30F01ADF4B13C98F966CEA86FA83EDCED891DCBE5567
c11=0x7AAFC4BD45A0EB0005B8F048807B80B1EF28CB2DA508ED706ABFF58FBAF2BD41
a00, a01, a10, a11, c00,c01,c10,c11, o, i = lode_fp4_mult(a00, a01, a10, a11, c00, c01, c10, c11)
d00,d01,d10,d11=fp4_mult(a00,a01,a10,a11,c00,c01,c10,c11)
d00 = Fp.czy(d00)
d01 = Fp.czy(d01)
d10 = Fp.czy(d10)
d11 = Fp.czy(d11)
print("c00=%X,\nc01=%X,\nc10=%X,\nc11=%X,\n"%(d00,d01,d10,d11))
'''


def lode_fp4_inv(a00, a01, a10, a11):
    a00, a01, a10, a11 = Fp(a00), Fp(a01), Fp(a10), Fp(a11)
    o = Fp(0)
    return a00, a01, a10, a11,  o


def fp4_inv(a00, a01, a10, a11):
    m100, m101 = fp2_mult(a00, a01, a00, a01)  # a0^2
    m200, m201 = fp2_mult(a10, a11, a10, a11)  # a1^2
    a200, a201 = fp2_add(m100, m101, o, o)
    t30, t31 = fp2_sub(o, m200, m201, o)
    m100, m101 = fp2_sub(t30, t31, m201, o)
    a100, a101 = fp2_sub(a200, a201, m100, m101)
    #t0
    t00, t01 = fp2_inv(a100, a101)
    a200, a201 = fp2_sub(o, o, a10, a11)
    c00, c01 = fp2_mult(t00, t01, a00, a01)
    c10, c11 = fp2_mult(t00, t01, a200, a201)

    return c00, c01, c10, c11
'''
#test_fp4_inv
a01  = 0x3CA03C51E4BD5B2952F7975DC4BA732591E225079160F3F67DCFA6F6840EC095
a00  = 0x5CECBFE01B025D57CC41A9AF3258D8FF29AFA7965969BF36D3BE9698E99C6EED
a11  = 0x2339B6764008293F648DEE90C9474E0868F1071F49E95B00757C6FF591A218F8
a10  = 0x79288FB51D662524BE7FA9E092CFCEE028E78E6B6132C1F8017DC791E0A3496F
c00=0x9F594F9C78FC3107C89B5721ACB00E66A73A4C873B92E52D34E857237187B8B1
c01=0x2094882EFA2DCE9052FB94C2B4058109F73149B36B35AB05FFB600F6444AB500
c10=0x5784CD0E3655F30C46FD30F01ADF4B13C98F966CEA86FA83EDCED891DCBE5567
c11=0x7AAFC4BD45A0EB0005B8F048807B80B1EF28CB2DA508ED706ABFF58FBAF2BD41
a00, a01, a10, a11, o = lode_fp4_inv(a00, a01, a10, a11)
c00,c01,c10,c11=fp4_inv(a00,a01,a10,a11)
print("c00=%X,\nc01=%X,\nc10=%X,\nc11=%X,\n"%(Fp.czy(c00),Fp.czy(c01),Fp.czy(c10),Fp.czy(c11)))
'''



##################################fp12 #######################################
def lode_fp12_mult(a0_00, a0_01, a0_10, a0_11, a1_00, a1_01, a1_10, a1_11, a2_00, a2_01, a2_10, a2_11,
                   b0_00, b0_01, b0_10, b0_11, b1_00, b1_01, b1_10, b1_11, b2_00, b2_01, b2_10, b2_11):
    a0_00, a0_01, a0_10, a0_11, a1_00, a1_01, a1_10, a1_11, a2_00, a2_01, a2_10, a2_11 = Fp(a0_00), Fp(a0_01),\
    Fp(a0_10), Fp(a0_11),Fp(a1_00), Fp(a1_01),Fp(a1_10), Fp(a1_11),Fp(a2_00), Fp(a2_01),Fp(a2_10), Fp(a2_11)
    b0_00, b0_01, b0_10, b0_11, b1_00, b1_01, b1_10, b1_11, b2_00, b2_01, b2_10, b2_11 = Fp(b0_00), Fp(b0_01), \
                                                                                         Fp(b0_10), Fp(b0_11), Fp(
        b1_00), Fp(b1_01), Fp(b1_10), Fp(b1_11), Fp(b2_00), Fp(b2_01), Fp(b2_10), Fp(b2_11)
    o = Fp(0)
    i = Fp(1)

    return a0_00, a0_01, a0_10, a0_11, a1_00, a1_01, a1_10, a1_11, a2_00, a2_01, a2_10, a2_11\
        , b0_00, b0_01, b0_10, b0_11, b1_00, b1_01, b1_10, b1_11, b2_00, b2_01, b2_10, b2_11, o,i
 
def fp12_mult(a0_00, a0_01, a0_10, a0_11, a1_00, a1_01, a1_10, a1_11, a2_00, a2_01, a2_10, a2_11,
              b0_00, b0_01, b0_10, b0_11, b1_00, b1_01, b1_10, b1_11, b2_00, b2_01, b2_10, b2_11):
    t00, t01, t10, t11 = fp4_mult(a2_00, a2_01, a2_10, a2_11, b2_00, b2_01, b2_10, b2_11)
    t100, t101, t110, t111 = fp4_add(a2_00, a2_01, a2_10, a2_11, a1_00, a1_01, a1_10, a1_11)
    t200, t201, t210, t211 = fp4_add(b2_00, b2_01, b2_10, b2_11, b1_00, b1_01, b1_10, b1_11)

    t300, t301, t310, t311 = fp4_mult(a1_00, a1_01, a1_10, a1_11, b1_00, b1_01, b1_10, b1_11)
    t400, t401, t410, t411 = fp4_add(a2_00, a2_01, a2_10, a2_11, a0_00, a0_01, a0_10, a0_11)
    t500, t501, t510, t511 = fp4_add(b2_00, b2_01, b2_10, b2_11, b0_00, b0_01, b0_10, b0_11)

    m00, m01, m10, m11 = fp4_mult(t100, t101, t110, t111, t200, t201, t210, t211)
    t600, t601, t610, t611 = fp4_add(a1_00, a1_01, a1_10, a1_11, a0_00, a0_01, a0_10, a0_11)
    t700, t701, t710, t711 = fp4_add(b1_00, b1_01, b1_10, b1_11, b0_00, b0_01, b0_10, b0_11)

    t100, t101, t110, t111 = fp4_mult(a0_00, a0_01, a0_10, a0_11, b0_00, b0_01, b0_10, b0_11)
    A00, A01, A10, A11 = fp4_sub(m00, m01, m10, m11, t00, t01, t10, t11)
    A00, A01, A10, A11 = fp4_sub(A00, A01, A10, A11, t300, t301, t310, t311)

    m00, m01, m10, m11 = fp4_add(A11, o, o, o, A11,o, o, o)
    m00, m01, m10, m11 = fp4_sub(o, A10, A00, A01, m00, m01, m10, m11)

    t200, t201, t210, t211 = fp4_mult(t600, t601, t610, t611, t700, t701, t710, t711)
    c0_00, c0_01, c0_10, c0_11 = fp4_add(m00, m01, m10, m11, t100, t101, t110, t111)

    m00, m01, m10, m11 = fp4_add(t11, o, o, o, t11, o, o, o)
    m00, m01, m10, m11 = fp4_sub(o, t10, t00, t01, m00, m01, m10, m11)
    t600, t601, t610, t611 = fp4_sub(t200, t201, t210, t211, t300, t301, t310, t311)
    t600, t601, t610, t611 = fp4_sub(t600, t601, t610, t611, t100, t101, t110, t111)

    t700, t701, t710, t711 = fp4_mult(t400, t401, t410, t411, t500, t501, t510, t511)
    c1_00, c1_01, c1_10, c1_11 = fp4_add(m00, m01, m10, m11, t600, t601, t610, t611)
    A00, A01, A10, A11 = fp4_sub(t700, t701, t710, t711, t00, t01, t10, t11)

    A00, A01, A10, A11 = fp4_sub(A00, A01, A10, A11, t100, t101, t110, t111)
    c2_00, c2_01, c2_10, c2_11 = fp4_add(A00, A01, A10, A11, t300, t301, t310, t311)
    return c0_00, c0_01, c0_10, c0_11, c1_00, c1_01, c1_10, c1_11, c2_00, c2_01, c2_10, c2_11


# test-fp12_mult

a2_11 = 0xB34B8E517F7E5DB0574079A4E75672BDDA113DA5629ECE7BF515DA6EF500CAA0
a2_10 = 0x78373FDBA495892160FD7A5421A8365160A7EE9E81687A13112CF0A0417A2EC3
a2_01 = 0x4B37945D66D8DEEF54C71E80C3CFD390EB175AF90A179F6989D6486B0BAB15AC
a2_00 = 0x19C8EB1027D6AEA5626EA89D9F8ED885CC8C5FE13E21864A5CC437E02BA6F88
a1_11 = 0x93AB07E341FB6A8772C01E11C702B770C3838F5615DB691D89ABE4D909E2B819
a1_10 = 0xA9C9C184C353A9BBC5DFB502231D93FB64EEEF44DB3776703AB1718024C04E62
a1_01 = 0x743D44BC31BF1152625D3716AA6BF77F03770F29DE408A895B6C6E6DBE3A9ED7
a1_00 = 0x9A70EC4EBA9671E05CA23EB701F3C605BEA401DAEC8EFA58AB53872649ED6771
a0_11 = 0x84586CF40A034AB24E321D56A3CEFBC38187C246897D22656054CA17EA44F86C
a0_10 = 0x361AF0FA39B34CF73D2016986B062BA6237C6E48882DEF4C45EBBBBC020F9A37
a0_01 = 0x38F7DB4BC62F5D8B2E513767F9711B4F37B9BA19138706D6CA2BB3DDA2065557
a0_00 = 0x85433C15BADBDBE4B677EB1E6894F73A81FDDE00382294B13A6E2264559BD0BF
b2_11 = 0x15EC7C8EED1B4A70BC759ABD4D152FFB6C12BB25B8DCFB0A933A9A4A5AD29B4D
b2_10 = 0x1A272001699AE668F92EA7C48569043F8225F1D4AA2718A952ECB9AD6FCADCC4
b2_01 = 0x92E2E15D5492571E9A3D81E3E7D779153BE570785B1834AAD99522BED682AA07
b2_00 = 0x1232151BACC17A51C5E7219E706D9581AD4A5810F8F39C17D02DD067BD279D7E
b1_11 = 0x8B6993B8458D1A30EFEE0DD36314F3A9BA22F2AA4E94D8447BFB6A3EF63F19B8
b1_10 = 0x3E3E6D58DA417FD72216DB17EA0EB36099AFBC17310BCECCF9CA3708F8E0071B
b1_01 = 0x53D3E4CA4C233591BCF0CE04360003F8DBE3D37D021FDB69BFCAD7CEF9A0F855
b1_00 = 0x104B83911DEFAC8263D8780A2DAFA4F91A12FD814827B681A419855FF1BF0FBD
b0_11 = 0x4AC979F5D90342CA3798D043FFEEA8020F585AA9C01AC1B7F5BC7C4AA355EBD6
b0_10 = 0x837BFDB822C32203D5923164874C339EC31986C990A938E23B23710EB7CFFA1A
b0_01 = 0x3B477D0248BB84E48A19656D26D214E0951F591272471FEAF6D90D9D1A0B7B0F
b0_00 = 0x3EA753E2EEBF4AC0DB45FF26D7FD33263B97B4EDAD57B493768CE7B33B7F1A2




a0_00, a0_01, a0_10, a0_11, a1_00, a1_01, a1_10, a1_11, a2_00, a2_01, a2_10, a2_11 \
    , b0_00, b0_01, b0_10, b0_11, b1_00, b1_01, b1_10, b1_11, b2_00, b2_01, b2_10, b2_11, o, i= lode_fp12_mult(a0_00, a0_01, a0_10, a0_11, a1_00, a1_01, a1_10, a1_11, a2_00, a2_01, a2_10, a2_11,\
                   b0_00, b0_01, b0_10, b0_11, b1_00, b1_01, b1_10, b1_11, b2_00, b2_01, b2_10, b2_11)
c0_00, c0_01, c0_10, c0_11, c1_00, c1_01, c1_10, c1_11, c2_00, c2_01, c2_10, c2_11=\
    fp12_mult(a0_00, a0_01, a0_10, a0_11, a1_00, a1_01, a1_10, a1_11, a2_00, a2_01, a2_10, a2_11,
              b0_00, b0_01, b0_10, b0_11, b1_00, b1_01, b1_10, b1_11, b2_00, b2_01, b2_10, b2_11)

c0_00, c0_01, c0_10, c0_11, c1_00, c1_01, c1_10, c1_11, c2_00, c2_01, c2_10, c2_11 = Fp.czy(c0_00), Fp.czy(c0_01),\
    Fp.czy(c0_10), Fp.czy(c0_11),Fp.czy(c1_00), Fp.czy(c1_01),Fp.czy(c1_10), Fp.czy(c1_11),Fp.czy(c2_00), Fp.czy(c2_01),Fp.czy(c2_10), Fp.czy(c2_11)

print("%X\n%X\n%X\n%X\n%X\n%X\n%X\n%X\n%X\n%X\n%X\n%X\n"%(c0_00, c0_01, c0_10, c0_11, c1_00, c1_01, c1_10, c1_11, c2_00, c2_01, c2_10, c2_11))




def lode_fp12_inv(a0_00, a0_01, a0_10, a0_11, a1_00, a1_01, a1_10, a1_11, a2_00, a2_01, a2_10, a2_11):
    a0_00, a0_01, a0_10, a0_11, a1_00, a1_01, a1_10, a1_11, a2_00, a2_01, a2_10, a2_11 = Fp(a0_00), Fp(a0_01),\
    Fp(a0_10), Fp(a0_11),Fp(a1_00), Fp(a1_01),Fp(a1_10), Fp(a1_11),Fp(a2_00), Fp(a2_01),Fp(a2_10), Fp(a2_11)

    o = Fp(0)

    return a0_00, a0_01, a0_10, a0_11, a1_00, a1_01, a1_10, a1_11, a2_00, a2_01, a2_10, a2_11\
        ,  o
def fp12_inv(a0_00, a0_01, a0_10, a0_11, a1_00, a1_01, a1_10, a1_11, a2_00, a2_01, a2_10, a2_11):
    t00, t01, t10, t11 = fp4_mult(a1_00, a1_01, a1_10, a1_11,a1_00, a1_01, a1_10, a1_11)   #t0=a1*a1
    m00, m01, m10, m11 = fp4_mult(a2_00, a2_01, a2_10, a2_11, a0_00, a0_01, a0_10, a0_11) #Mreg=a2*a0
    t100, t101, t110, t111 = fp4_sub(t00, t01, t10, t11, m00, m01, m10, m11)
    m00, m01, m10, m11 = fp4_mult(a2_00, a2_01, a2_10, a2_11, a2_00, a2_01, a2_10, a2_11)
    t200, t201, t210, t211 = fp4_add(m11, o, o, o, m11, o, o, o)
    t200, t201, t210, t211 = fp4_sub(o, m10, m00, m01, t200, t201, t210, t211)
    m00, m01, m10, m11 = fp4_mult(a1_00, a1_01, a1_10, a1_11, a0_00, a0_01, a0_10, a0_11)
    t300, t301, t310, t311 = fp4_sub(t200, t201, t210, t211, m00, m01, m10, m11)
    t00, t01, t10, t11 = fp4_mult(a0_00, a0_01, a0_10, a0_11, a0_00, a0_01, a0_10, a0_11)
    m00, m01, m10, m11 = fp4_mult(a2_00, a2_01, a2_10, a2_11, a1_00, a1_01, a1_10, a1_11)
    m100, m101, m110, m111 = fp4_add(m11, o, o, o, m11, o, o, o)
    m00, m01, m10, m11 = fp4_sub(o, m10, m00, m01, m100, m101, m110, m111)
    t400, t401, t410, t411 = fp4_sub(t00, t01, t10, t11, m00, m01, m10, m11)
    m00, m01, m10, m11 = fp4_mult(a1_00, a1_01, a1_10, a1_11, t100, t101, t110, t111)
    t200, t201, t210, t211 = fp4_add(m11, o, o, o, m11, o, o, o)
    t500, t501, t510, t511 = fp4_sub(o, m10, m00, m01, t200, t201, t210, t211)
    m00, m01, m10, m11 = fp4_mult(a0_00, a0_01, a0_10, a0_11, t400, t401, t410, t411)
    t600, t601, t610, t611 = fp4_add(t500, t501, t510, t511, m00, m01, m10, m11)
    m00, m01, m10, m11 = fp4_mult(a2_00, a2_01, a2_10, a2_11, t300, t301, t310, t311)
    t200, t201, t210, t211 = fp4_add(m11, o, o, o, m11, o, o, o)
    m00, m01, m10, m11 = fp4_sub(o, m10, m00, m01, t200, t201, t210, t211)
    a00, a01, a10, a11 = fp4_add(t600, t601, t610, t611, m00, m01, m10, m11)
    #t7
    t700, t701, t710, t711 = fp4_inv(a00, a01, a10, a11)
    c2_00, c2_01, c2_10, c2_11 = fp4_mult(t100, t101, t110, t111, t700, t701, t710, t711)
    c1_00, c1_01, c1_10, c1_11 = fp4_mult(t300, t301, t310, t311, t700, t701, t710, t711)

    c0_00, c0_01, c0_10, c0_11 = fp4_mult(t400, t401, t410, t411, t700, t701, t710, t711)


    return c0_00, c0_01, c0_10, c0_11, c1_00, c1_01, c1_10, c1_11, c2_00, c2_01, c2_10, c2_11
'''
#test fp12_inv
a0_00=0x2543D04C9FEA0B04741B8852ACE7D7E266F51C611282C78C1F4F90F396CA9634
a0_01=0x4A5F5504B8A26D0ED22EA0BDC94139AEECCE56F877CDA51D97E5B9AE482F13D4
a0_10=0x187FC8C9076ADCF9D78784EA0EA794471C5D0ECC6366E6DEB4B9525D9603DF0A
a0_11=0x15262F4AE3A5382EEF37841BC9320D18FCFB6C06B2D563D39DC869F7D251B70
a1_00=0x407C4EADF2BF5A436956D1CE076DEB0FEA8FB43E20617A8E673A13DFB5D3864D
a1_01=0x2CA2EE45CF2F8AA4952C5D168C93517AB719654A3357C01EF033F190EAE7259D
a1_10=0x4EA248DD18F86DA4259076A2B6FCC34DB762821993E03F0057E78EAB2DB76C6D
a1_11=0x84AEFC349B8FCFAA012429BA8400CD8EAF44B49E94AD1B6EFE57879B48D48142
a2_00=0x17AA5CD1D5B26D13D633BBFC662BB62A760C377307ABA8CCDA6FB6315AA03930
a2_01=0x476DF630BF6B1A9734EBB3832AE1EDEF84FC14C91090CE742E871630D73BEF67
a2_10=0x7D4824B43C744966A7B273E7FC1DABF5EA38D93206F3E8051B43E74A414AF026
a2_11=0x85433C15BADBDBE4B677EB1E6894F73A81FDDE00382294B13A6E2264559BD0BF
a0_00, a0_01, a0_10, a0_11, a1_00, a1_01, a1_10, a1_11, a2_00, a2_01, a2_10, a2_11 \
    , o = lode_fp12_inv(a0_00, a0_01, a0_10, a0_11, a1_00, a1_01, a1_10, a1_11, a2_00, a2_01, a2_10, a2_11)
c0_00, c0_01, c0_10, c0_11, c1_00, c1_01, c1_10, c1_11, c2_00, c2_01, c2_10, c2_11=\
    fp12_inv(a0_00, a0_01, a0_10, a0_11, a1_00, a1_01, a1_10, a1_11, a2_00, a2_01, a2_10, a2_11)

c0_00, c0_01, c0_10, c0_11, c1_00, c1_01, c1_10, c1_11, c2_00, c2_01, c2_10, c2_11 = Fp.czy(c0_00), Fp.czy(c0_01), \
                                                                                     Fp.czy(c0_10), Fp.czy(
    c0_11), Fp.czy(c1_00), Fp.czy(c1_01), Fp.czy(c1_10), Fp.czy(c1_11), Fp.czy(c2_00), Fp.czy(c2_01), Fp.czy(
    c2_10), Fp.czy(c2_11)
print("%X\n%X\n%X\n%X\n%X\n%X\n%X\n%X\n%X\n%X\n%X\n%X\n"%(c0_00, c0_01, c0_10, c0_11, c1_00, c1_01, c1_10, c1_11, c2_00, c2_01, c2_10, c2_11))

'''

##################################point_adder_fp2 #######################################
def lode_point_adder_fp2(XT0, XT1, YT0, YT1, ZT0, ZT1, XQ0, XQ1, YQ0, YQ1, ZQ0, ZQ1, xp,yp):
    XT0, XT1, YT0, YT1, ZT0, ZT1, XQ0, XQ1, YQ0, YQ1, ZQ0, ZQ1 = Fp(XT0), Fp(XT1),\
    Fp(YT0), Fp(YT1),Fp(ZT0), Fp(ZT1),Fp(XQ0), Fp(XQ1),Fp(YQ0), Fp(YQ1),Fp(ZQ0), Fp(ZQ1)
    xp, yp = Fp(xp), Fp(yp)
    o = Fp(0)
    i = Fp(1)

    return XT0, XT1, YT0, YT1, ZT0, ZT1, XQ0, XQ1, YQ0, YQ1, ZQ0, ZQ1, xp,yp, o, i



def point_adder_fp2(XT0,XT1,YT0,YT1,ZT0,ZT1,XQ0,XQ1,YQ0,YQ1,ZQ0,ZQ1,xp,yp):

    t00,t01=fp2_mult(ZT0,ZT1,ZT0,ZT1) #t0=ZT*ZT
    t10,t11=fp2_mult(YQ0,YQ1,ZT0,ZT1) #t1=YQ*ZT   line1

    t10,t11=fp2_mult(t00,t01,t10,t11) #t1=t0*t1
    t20,t21=fp2_mult(XQ0,XQ1,t00,t01) #t2=XQ*t0   line2

    t30,t31=fp2_sub(t20,t21,XT0,XT1) #t3=t2-XT
    t40,t41=fp2_sub(t10,t11,YT0,YT1) #t4=t1-YT   lin3

    t50,t51=fp2_mult(t30,t31,t30,t31)#t5=t3*t3
    XR0,XR1=fp2_mult(t40,t41,t40,t41)#XR=t4*t4   lin4

    t60,t61=fp2_mult(t30,t31,t50,t51)#t6=t3*t5
    ZR0,ZR1=fp2_mult(ZT0,ZT1,t30,t31)#ZR=ZT*t3   lin5

    t70,t71=fp2_mult(XT0,XT1,t50,t51)#t7=XT*t5
    t20,t21=fp2_mult(XQ0,XQ1,t40,t41)#t2=XQ*t4   line6

    XR0,XR1=fp2_sub(XR0,XR1,t60,t61)#XR=XR-t6
    t10,t11=fp2_add(t70,t71,t70,t71)#t1=t7+t7   line7

    t60,t61=fp2_mult(YT0,YT1,t60,t61)#t6=YT*t6
    t30,t31=fp2_mult(YQ0,YQ1,ZR0,ZR1)#t3=YQ*ZR   line8

    XR0,XR1=fp2_sub(XR0,XR1,t10,t11)#XR=XR-t1
    l0_10,l0_11=fp2_sub(t20,t21,t30,t31)#l0=t2-t3   line9

    t20,t21=fp2_sub(t70,t71,XR0,XR1)#t2=t7-XR
    t30,t31=fp2_sub(o,o,t40,t41)#t3=-t4     line10

    t00,t01=fp2_mult(ZR0,ZR1,yp,o)#t0=ZR*yp
    l2_10,l2_11=fp2_mult(xp,o,t30,t31)#l2=xp*t3*v line11

    l0_00,l0_01=fp2_mult(t00,t01,o,i)#l0=l0+t0*kexi
    YR0,YR1=fp2_mult(t20,t21,t40,t41)#YR=t2*t4   line12

    YR0,YR1=fp2_sub(YR0,YR1,t60,t61)#YR=YR-t6

    return XR0,XR1,YR0,YR1,ZR0,ZR1,l2_10,l2_11,l0_10,l0_11,l0_00,l0_01

'''
XT0=0x7a3403e7e340c5fee8050fa05f5e2f8d32171c2b340c62fb569e0a4751f1c866
XT1=0x77c7e5d710d8e3c75b939c214ed90b42554b2bdaf537d0c3f7864c6f3f82654b
YT0=0x12d9351ac2f5eb92e675305cfb53c0cf396a31075f471a5474316a37879c441
YT1=0x215569af5ba8c2ce72a448800c86146b1b2148568ab6acb97a8173e02886d8d4
ZT0=0x7627e1a047d748c115f0ffce9057ee19014c24179ac575c3f2bf613c72d8285a
ZT1=0x172daf1d2d488c8545a2518b1d8bbf6804a9105716d07c9f864db4c940e45ffe
XQ0=0x29dba116152d1f786ce843ed24a3b573414d2177386a92dd8f14d65696ea5e32
XQ1=0x9f64080b3084f733e48aff4b41b565011ce0711c5e392cfb0ab1b6791b94c408
YQ0=0x41e00a53dda532da1a7ce027b7a46f741006e85f5cdff0730e75c05fb4e3216d
YQ1=0x69850938abea0112b57329f447e3a0cbad3e2fdb1a77f335e89e1408d0ef1c25
ZQ0=0x1
ZQ1=0x0
xp=0x93de051d62bf718ff5ed0704487d01d6e1e4086909dc3280e8c4e4817c66dddd
yp=0x21fe8dda4f21e607631065125c395bbc1c1c00cbfa6024350c464cd70a3ea616

XR0=419e0b33022473ffe9c8b288efc94dd698f327f1c4c3dc36a0fc343feaed3eda
XR1=a8ff0a1b67f67794c1e3041ccf2332b73c2bc3eae2bb8fda6c5a400b8208335d
YR0=40269e2edc0cd089ad7d1f66ee82d1e7057e74422a9554633d249c0ff35b135b
YR1=2da7584d22ce64f6efcc2fec7f8899188cc846ba5b8e2c046da48b721382f960
ZR0=792edd63b858aac462fff70a5174aaabd6289fc3604e5d18653a90b059476566
ZR1=6ebd384a6c3107ed7f2e71866e910603a9ff7bccc4026291b5d1500a112b39fa
l2_10=7d5b3342e7e3fa5fe6e9e8ae2429673ceccb432e800a43d83f14de79397c2416
l2_11=a0b2e8fa4e814504172c3a40d0535ca4a0789c99c6df8d0ebed6bd8d0933a14e
l2_11=523882ae621d95567232f4c29be736f9e2c22922f324dc1e90b63e3c6deb0f9a
l2_11=963a4133ad15be90e56adf511b4c72bfb31cc72fd55b5df9414bbfc23c32bbc3
l2_11=646575d8bbaeb3a7d4ed40984a747771851eee8895c320df3878bd5653a3ef7e
l2_11=6689f8143bb5980b31dea40a1e066111c2d1dcd514382d6abb188dd444ddbe4c
XT0, XT1, YT0, YT1, ZT0, ZT1, XQ0, XQ1, YQ0, YQ1, ZQ0, ZQ1, xp,yp, o, i = lode_point_adder_fp2(XT0, XT1, YT0, YT1, ZT0, ZT1, XQ0, XQ1, YQ0, YQ1, ZQ0, ZQ1, xp,yp)
XR0,XR1,YR0,YR1,ZR0,ZR1,l2_10,l2_11,l0_10,l0_11,l0_00,l0_01 = point_adder_fp2(XT0,XT1,YT0,YT1,ZT0,ZT1,XQ0,XQ1,YQ0,YQ1,ZQ0,ZQ1,xp,yp)
print("XR0=%x\nXR1=%x\nYR0=%x\nYR1=%x\nZR0=%x\nZR1=%x\nl2_10=%x\nl2_11=%x\nl2_11=%x\nl2_11=%x\nl2_11=%x\nl2_11=%x\n" % \
      (Fp.czy(XR0), Fp.czy(XR1), Fp.czy(YR0), Fp.czy(YR1), Fp.czy(ZR0), Fp.czy(ZR1), Fp.czy(l2_10), Fp.czy(l2_11), Fp.czy(l0_10), Fp.czy(l0_11), Fp.czy(l0_00), Fp.czy(l0_01)))
'''
##################################point_double_fp2 #######################################
def lode_point_double_fp2(XT0, XT1, YT0, YT1, ZT0, ZT1,  xp,yp):
    XT0, XT1, YT0, YT1, ZT0, ZT1 = Fp(XT0), Fp(XT1), Fp(YT0), Fp(YT1), Fp(ZT0), Fp(ZT1)
    xp, yp = Fp(xp), Fp(yp)
    o = Fp(0)
    i = Fp(1)

    return XT0, XT1, YT0, YT1, ZT0, ZT1, xp,yp, o, i
def point_double_fp2(XT0, XT1, YT0, YT1, ZT0, ZT1, xp, yp):

    t00, t01 = fp2_mult(XT0, XT1, XT0, XT1)  # t0=XT*XT
    t10, t11 = fp2_mult(YT0, YT1, YT0, YT1)  # t1=YT*YT

    t20, t21 = fp2_add(t00, t01, t00, t01)  # t2=t0+t0
    t30, t31 = fp2_add(XT0, XT1, XT0, XT1)  # t3=XT+XT

    t00, t01 = fp2_add(t00, t01, t20, t21)  # t0=t0+t2
    t30, t31 = fp2_add(t30, t31, t30, t31)  # t3=t3+t3

    t20, t21 = fp2_mult(t10, t11, t10, t11)  # t2=t1*t1
    t30, t31 = fp2_mult(t10, t11, t30, t31)  # t3=t1*t3

    t40, t41 = fp2_mult(ZT0, ZT1, ZT0, ZT1)  # t4=ZT*ZT
    XR0, XR1 = fp2_mult(t00, t01, t00, t01)  # XR=t0*t0

    t20, t21 = fp2_add(t20, t21, t20, t21)  # t2=t2+t2
    XR0, XR1 = fp2_sub(XR0, XR1, t30, t31)  # XR=XR-t3

    t20, t21 = fp2_add(t20, t21, t20, t21)  # t2=t2+t2
    XR0, XR1 = fp2_sub(XR0, XR1, t30, t31)  # XR=XR-t3

    t20, t21 = fp2_add(t20, t21, t20, t21)  # t2=t2+t2
    YR0, YR1 = fp2_sub(t30, t31, XR0, XR1)  # YR=t3-XR

    YR0, YR1 = fp2_mult(t00, t01, YR0, YR1)  # YR=t0*YR
    ZR0, ZR1 = fp2_mult(YT0, YT1, ZT0, ZT1)  # ZR=YT*ZT

    ZR0, ZR1 = fp2_add(ZR0, ZR1, ZR0, ZR1)  # ZR=ZR+ZR
    t10, t11 = fp2_add(t10, t11, t10, t11)  # t1=t1+t1

    t30, t31 = fp2_mult(ZR0, ZR1, t40, t41)  # t3=-ZR*t4
    t30, t31 = fp2_sub(o, o, t30, t31)
    t50, t51 = fp2_mult(t00, t01, XT0, XT1)  # t5=t0*XT

    YR0, YR1 = fp2_sub(YR0, YR1, t20, t21)  # YR=YR-t2
    l0_10, l0_11 = fp2_sub(t10, t11, t50, t51)  # l01=(t1-t5)v

    t30, t31 = fp2_mult(t30, t31, yp, o)  # t3=t3*yp
    t00, t01 = fp2_mult(t00, t01, t40, t41)  # t0=t0*t4

    l0_00, l0_01 = fp2_mult(t30, t31, o, i)  # l00=t3*kexi
    l2_10, l2_11 = fp2_mult(t00, t01, xp, o)  # l21=t0*xp  modified
    return XR0, XR1, YR0, YR1, ZR0, ZR1, l2_10, l2_11, l0_10, l0_11, l0_00, l0_01
'''
XT0=0x29dba116152d1f786ce843ed24a3b573414d2177386a92dd8f14d65696ea5e32
XT1=0x9f64080b3084f733e48aff4b41b565011ce0711c5e392cfb0ab1b6791b94c408
YT0=0x41e00a53dda532da1a7ce027b7a46f741006e85f5cdff0730e75c05fb4e3216d
YT1=0x69850938abea0112b57329f447e3a0cbad3e2fdb1a77f335e89e1408d0ef1c25
ZT0=0x1
ZT1=0x0
xp=0x93de051d62bf718ff5ed0704487d01d6e1e4086909dc3280e8c4e4817c66dddd
yp=0x21fe8dda4f21e607631065125c395bbc1c1c00cbfa6024350c464cd70a3ea616

XR0=21d7ca9df02db97529552efbc9146ca1c0f9df61a21ad879c238641c3e1fe7e7
XR1=b20e2ac9a09ab2e8641be8155c3e1e2461cd5e5afc6a61164f211db96369ae00
YR0=5d46188f5d9cd15aab47d41fb77ff74a9b668a13baffe468316bd6c7a7606ed8
YR1=84a1137b13a442e6b89520fbc7b80262e773dfcba0775fd92b16f9c0c4278c44
ZR0=83c014a7bb4a65b434f9c04f6f48dee8200dd0beb9bfe0e61ceb80bf69c642da
ZR1=1cca127155305b3394e2a8989a387a523889cc6b1a74f78febcc8ce9be8cf2cd
l2_10=559e9bc77916a02dba099d8aeed75cadae8083ac449e6f6261b589eedbd24e20
l2_11=633ced3b9d4d7be968a9bcbb2e4be46286deddc2a678779b1f5509be35d33b5d
l2_11=216fce23185f4fafb1fbdbee537d5ff9a43494c6c6a93f8db6ef5f2e8b5a9de5
l2_11=4de94cdc4efa2a62a8d628c3449a48e2bfbadc09a0e6ed5c9a81c05ef4b9933a
l2_11=694bb229f0c379d1c87b5a2956ac56fbdba25c4958fe62e7567c75eddfd5b13a
l2_11=207b9fdba11f5a71418f63c4b2252e19e3166918e5a344d7006ba39619930184
XT0, XT1, YT0, YT1, ZT0, ZT1, xp,yp, o, i = lode_point_double_fp2(XT0, XT1, YT0, YT1, ZT0, ZT1,  xp,yp)
XR0, XR1, YR0, YR1, ZR0, ZR1, l2_10, l2_11, l0_10, l0_11, l0_00, l0_01 = point_double_fp2(XT0, XT1, YT0, YT1, ZT0, ZT1, xp, yp)
print("XR0=%x\nXR1=%x\nYR0=%x\nYR1=%x\nZR0=%x\nZR1=%x\nl2_10=%x\nl2_11=%x\nl2_11=%x\nl2_11=%x\nl2_11=%x\nl2_11=%x\n" % \
      (Fp.czy(XR0), Fp.czy(XR1), Fp.czy(YR0), Fp.czy(YR1), Fp.czy(ZR0), Fp.czy(ZR1), Fp.czy(l2_10), Fp.czy(l2_11), Fp.czy(l0_10), Fp.czy(l0_11), Fp.czy(l0_00), Fp.czy(l0_01)))
'''