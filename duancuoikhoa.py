import streamlit as st
st.set_page_config(page_title='Vương quốc Skibidi', page_icon='✨')

with st.sidebar:
    st.title('Vương quốc Skibidi')
    st.header('Chào mừng bạn đến với Vương quốc Skibidi!')
    st.image('pic1.jpg') 
    st.write('Chúng tôi chuyên bán các sản phẩm cực hot: Iphone 17 pro max, Lightstick J97, Kẹo rau củ Kera và nhựa HDPE.')
    st.write(':house: Địa chỉ cửa hàng: Hoàn Long, Yên Mỹ, Hưng Yên')
    st.write(':phone: Điện thoại liên hệ: 0123456789')

st.title('Vương quốc Skibidi')
coll, col2 = st.columns(2)

with coll:
    b1 = st.button('Đồ công nghệ & Idol')
with col2:
    b2 = st.button('Thực phẩm & Vật liệu')

if b1:
    st.header('Danh sách Đồ công nghệ & Idol')
    c1, c2 = st.columns(2)
    with c1:
        st.image('pic2.jpg', caption='Iphone 17 pro max - Mã số: 001')
    with c2:
        st.image('pic3.jpg', caption='Lightstick J97 - Mã số: 002')

if b2:
    st.header('Danh sách Thực phẩm & Vật liệu')
    c3, c4 = st.columns(2)
    with c3:
        st.image('pic4.jpg', caption='Kẹo rau củ Kera - Mã số: 003')
    with c4:
        st.image('pic5.jpg', caption='Nhựa HDPE - Mã số: 004')

st.header('Đặt hàng')
with st.form('Đơn đặt hàng'):
    topics = ('Iphone 17 pro max', 'Lightstick J97', 'Kẹo rau củ Kera', 'nhựa HDPE')
    option_topic = st.selectbox('Sản phẩm bạn chọn', topics)
    
    codes = ('001', '002', '003', '004')
    option_code = st.selectbox('Mã số sản phẩm', codes)
    
    nums = st.slider('Số lượng bạn muốn đặt:', 0, 10, 0)
    name = st.text_input('Họ và tên')
    phone = st.text_input('Số điện thoại nhà riêng')
    address = st.text_input('Địa chỉ giao hàng')
    
    bill = {
        'Loại sản phẩm:': option_topic,
        'Mã số:': option_code,
        'Số lượng:': nums,
        'Họ tên khách hàng:': name,
        'Số điện thoại liên hệ:': phone,
        'Địa chỉ giao hàng:': address
    }
    
    submitted = st.form_submit_button('Xác nhận')
    if submitted:
        st.header('Bạn đã chọn:')
        for x, y in bill.items():
            st.write(x, y)

print_bill = st.checkbox('In hoá đơn')
if print_bill:
    ans = ''
    for x in bill:
        ans += str(x) + ' ' + str(bill[x]) + '\n'
    st.download_button('Tải hóa đơn về máy', ans, file_name='hoa_don.txt')