#encoding:utf-8
"""将waf文件夹放入网站根目录,执行python脚本"""
import os

def write_waf(path):#参数为网站目录绝对路径
    dirs = os.listdir(path)
    for d in dirs:
#       print d
        child_p = os.path.join(path,d).replace('\\','/')
        if os.path.isdir(child_p):
            print '[*]Find out dir %s' % child_p
            write_waf(child_p)
        elif d[-3::] == 'php':
            try:
                _write_file(child_p)
                print '[*]Writed php file %s' % child_p
            except :
                print '[*]Write %s Error,Please check Permission' % child_p
def _write_file(child_p):
    with open(child_p) as f:
        if "<?php @include('/waf/waf.php');?>" in f.read():
            return 0
        lines = f.readlines()
    with open(child_p,'w') as f:
        f.write("<?php @include('/waf/waf.php');?>\n")
    with open(child_p,'a') as f:
        for line in lines:
            f.write(line)
if __name__ == "__main__":
#   print dir(os)
    write_waf('C:/Users/dell-1/Desktop/code/PHP/WAF/test1')