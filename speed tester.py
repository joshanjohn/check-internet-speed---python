import speedtest

st = speedtest.Speedtest()

opt = int(input('what to test ?'))

'''
    1) DOwnloading speed 
    2) Uploading speed

    '''
if opt == 1:
    print(st.download())

elif opt == 2:
    print(st.upload())

else:
    print('INVALID OPTION')

