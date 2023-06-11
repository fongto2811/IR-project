# IR - project

#### **GVHD:** ThS. Quách Đình Hoàng
#### **SVTH:**
* Nguyễn Minh Luân - 19110395
* Tô Thanh Phong - 19110050
* Tôn Thiên Thạch - 19110455
* Đào Quyết Phong - 19110427

*Link github: https://github.com/fongto2811/IR-project

### 1. Abstract (Tóm tắt)

* Nhận thấy, ngành thương mại điện tử đang phát triển trong thời đại hiện nay. Một lượng dữ liệu khổng lồ được sinh ra từ các sản phẩm, mặt hàng rất đa dạng trên các nền tảng này. Điều đó tạo nên những mặt tốt để khai thác nguồn dữ liệu này cho đề tài của nhóm. Một trong những nơi có thể khai thác được nguồn dữ liệu từ các hoạt động trên đến từ các sàn giao dịch thương mại điện tử, chợ thương mại điển tử như  Shopee, Lazada, Tiki,... nhưng website này có một lượng lớn người cung cấp sản phẩm (người bán) và người tiêu dùng (người mua) truy cập và giao dịch mỗi ngày. Từ đó, nhóm tôi quyết định chọn 01 trong những sàn thương mại điện tử tốt nhất hiện nay – sàn Amazon, làm đối tượng chính để khai thác dữ liệu. Đề tài của nhóm là áp dụng kiến thức đã học, thực hành về information retrieval để xây dựng một Search Engine dùng Elasticsearch trên tập dữ liệu sản phẩm thu thập được trên Sàn thương mại điện tử Amazon (website – amazon.com) với kỹ thuật web scraping và ứng dụng elasticsearch

### 2. Introduction (Giới thiệu)

* Sàn thương mại điện tử Amazon là một trong những sàn thương mại điện tử lớn nhất thế giới thế giới với hàng triệu sản phẩm được bán trên trang web của họ. Nhưng việc tìm kiếm những sản phẩm phù hợp trên Amazon đôi khi có thể gây khó khăn cho người dùng. Vì vậy, nhóm đã xây dựng 01 công cụ tìm kiếm – search engine trên Amazon để giúp cho người dùng tìm kiếm những sản phẩm phù hợp.
* Mục đích của search engine này được thiết kế để giúp người dùng có thể tìm kiếm và phân loại sản phẩm một cách dễ dàng và hiệu quả. Công cụ này cung cấp cho người dùng một loạt các tính năng tìm kiếm để giúp người dùng tìm kiếm sản phẩm theo nhu cầu của mình.
* Ngoài ra, nó còn cho phép người dùng phân loại kết quả tìm kiếm theo nhiều tiêu chí khác nhau như giá cả, đánh giá sao của khách hàng, danh mục sản phẩm. Điều này giúp người dùng có thể lọc danh sách sản phẩm theo nhu cầu của họ và tìm kiếm sản phẩm phù hợp một cách nhanh chóng và dễ dàng.
* Thêm vào đó, search engine cũng cung cấp cho người dùng các tính năng tìm kiếm khác như tìm kiếm sản phẩm theo thương hiệu, phiên bản sản phẩm và các sản phẩm liên quan.
* Kết luận, search engine trên sàn thương mại điện tử Amazon mà nhóm xây dựng với kỳ vọng là một công cụ quan trọng và cần thiết đối với việc tìm kiếm sản phẩm trên website của Amazon, giúp việc tìm kiếm đa dạng chủng loại sản phẩm và thuận tiện cho người dùng khi sử dụng.

### 3. Data (Tập Dữ liệu)

***Giới thiệu về dữ liệu***: hiện tại Amazon đang lưu trữ dữ liệu của 385 triệu sản phẩm tiêu dùng *(theo thống kê từ sellerengine.com)*. Với lượng sản phẩm rất lớn này Amazon đã chia nhỏ thành các mặt hàng (categories) để dễ dàng phân loại và tìm kiếm, với *30 mặt hàng*, trong đó 10 mặt hàng phố biển về mặt tiêu dùng như sau:
*	Home and Kitchen – 40%
*	Sports and Outdoors – 21%
*	Toys and Games – 19%
*	Beauty and Personal Care – 19%
*	Health, Household, and Baby Care – 18%
*	Kitchen and Dining – 16%
*	Office Products – 15%
*	Garden and Outdoor – 14%
*	Tools and Home Improvement – 14%
*	Pet Supplies – 13%
(theo số liệu năm 2022 từ https://nuoptima.com/blog/amazon-product-categories )

Như vậy, giả sử chúng ta chỉ cần khai thác một mặt hàng “Home & Kitchen” (các sản phẩm gia dụng, bếp núc) thì cũng chiếm 40%, tức 154 triệu sản phẩm. Vì dữ liệu thu thập là các mặt hàng, sản phẩm nên đây sẽ là **một số thuộc tính cơ bản** mà nhóm sẽ thu thập từ Amazon:

### 4. Design and Implementation (Thiết kế và thực thi)
#### 4.1. Web Scraping: nhóm sử dụng kỹ thuật này để lấy dữ liệu sản phẩm từ trang thương mại điện tử Amazon

1. Thêm thư viện [Selenium](https://www.selenium.dev/) và các thư viện cần thiết khác.
2. Định nghĩa các biến `URL` tới trang chủ amazon, `SESSION` phục vụ ghi log
3. Tạo file log
4. Khởi chạy Chrome, truy cập trang chủ amazon, ghi log
5. Danh sách các danh mục sản phẩm trên amazon
6. Định nghĩa các hàm để lưu đường dẫn đến các sản phẩm trên amazon
7. Lưu tất cả sản phẩm thuộc của mỗi danh mục
8. Đóng file log và Chrome

Chi tiết code tại file: [amazon-scrapping.ipynb](https://github.com/fongto2811/IR-project/blob/f15c1474830e67bf32c7c3bab5415ebac8812e59/amazon-scrapping.ipynb)
