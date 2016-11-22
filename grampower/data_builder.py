from grampower.service import StoreService
import config
from grampower.utils import singleton

@singleton
class DataBuilderService():
    
    __store_service = StoreService()

    def data_builder(self):
        
        store1 = {
                  "name":"prakash",
                  "street_address":"123-A, Rohini delhi",
                  "postal_code":"110089",
                  "city":"delhi",
                  "country":"India",
                  "contact_number":"8447673122",
                  "description":"Shop for beautiful wedding wear online, designed by Manyavar, a leading celebration wear brand for men across India. Buy men's suits, sherwani & wedding ",
                  "cover_image":"https://s-media-cache-ak0.pinimg.com/originals/bc/0a/6b/bc0a6bfd3855ebbe25b409df516287a9.jpg",
                  "licence_no":"134",
                  "thumbnails":["http://www.gettyimages.pt/gi-resources/images/Homepage/Hero/PT/PT_hero_42_153645159.jpg","http://www.gettyimages.ca/gi-resources/images/Homepage/Hero/UK/CMS_Creative_164657191_Kingfisher.jpg"],
                  "latitude":"22.456789056",
                  "longitude":"28.98765458"
        
                }
        self.__store_service.register(store1)
        
        store2 = {
                  "name":"prakash",
                  "street_address":"123-A, Rohini delhi",
                  "postal_code":"110089",
                  "city":"delhi",
                  "country":"India",
                  "contact_number":"8447673122",
                  "description":"Shop for beautiful wedding wear online, designed by Manyavar, a leading celebration wear brand for men across India. Buy men's suits, sherwani & wedding ",
                  "cover_image":"https://s-media-cache-ak0.pinimg.com/originals/bc/0a/6b/bc0a6bfd3855ebbe25b409df516287a9.jpg",
                  "licence_no":"1345",
                  "thumbnails":["http://2.bp.blogspot.com/-5Z4VfB7sDVs/T-u_Ixwx4uI/AAAAAAAAEqc/GDHoi_OjAXM/s1600/Tiger+3D+Wallpapers+3.jpg"],
                  "latitude":"22.456789056",
                  "longitude":"28.98765458"
        
                }
        self.__store_service.register(store2)
#         
#         store3 = {
#                   "name":"kumar",
#                   "street_address":"123-A, Rohini delhi",
#                   "postal_code":"110089",
#                   "city":"delhi",
#                   "country":"India",
#                   "contact_number":"8447673122",
#                   "description":"Shop for beautiful wedding wear online, designed by Manyavar, a leading celebration wear brand for men across India. Buy men's suits, sherwani & wedding ",
#                   "cover_image":"https://s-media-cache-ak0.pinimg.com/originals/bc/0a/6b/bc0a6bfd3855ebbe25b409df516287a9.jpg",
#                   "licence_no":"3"
#                 }
#         self.__store_service.register(store3)
#         
#         store4 = {
#                   "name":"kumar meg",
#                   "street_address":"123-A, Rohini delhi",
#                   "postal_code":"110089",
#                   "city":"delhi",
#                   "country":"India",
#                   "contact_number":"8447673122",
#                   "description":"Shop for beautiful wedding wear online, designed by Manyavar, a leading celebration wear brand for men across India. Buy men's suits, sherwani & wedding ",
#                   "cover_image":"https://s-media-cache-ak0.pinimg.com/originals/bc/0a/6b/bc0a6bfd3855ebbe25b409df516287a9.jpg",
#                   "licence_no":"4"
#                 }
#         self.__store_service.register(store4)
#         
#         store5 = {
#                   "name":"ghazala",
#                   "address":"123 reaction",
#                   "licence_no":"5"
#                 }
#         self.__store_service.register(store5)
#         
#         store6 = {
#                   "name":"ghazala p",
#                   "street_address":"123-A, Rohini delhi",
#                   "postal_code":"110089",
#                   "city":"delhi",
#                   "country":"India",
#                   "contact_number":"8447673122",
#                   "description":"Shop for beautiful wedding wear online, designed by Manyavar, a leading celebration wear brand for men across India. Buy men's suits, sherwani & wedding ",
#                   "cover_image":"https://s-media-cache-ak0.pinimg.com/originals/bc/0a/6b/bc0a6bfd3855ebbe25b409df516287a9.jpg",
#                   "licence_no":"6"
#                 }
#         self.__store_service.register(store6)
#         
#         store7 = {
#                   "name":"nand ji",
#                   "street_address":"123-A, Rohini delhi",
#                   "postal_code":"110089",
#                   "city":"delhi",
#                   "country":"India",
#                   "contact_number":"8447673122",
#                   "description":"Shop for beautiful wedding wear online, designed by Manyavar, a leading celebration wear brand for men across India. Buy men's suits, sherwani & wedding ",
#                   "cover_image":"https://s-media-cache-ak0.pinimg.com/originals/bc/0a/6b/bc0a6bfd3855ebbe25b409df516287a9.jpg",
#                   "licence_no":"7"
#                 }
#         self.__store_service.register(store7)
#         
#         store8 = {
#                   "name":"Ankit",
#                   "street_address":"123-A, Rohini delhi",
#                   "postal_code":"110089",
#                   "city":"delhi",
#                   "country":"India",
#                   "contact_number":"8447673122",
#                   "description":"Shop for beautiful wedding wear online, designed by Manyavar, a leading celebration wear brand for men across India. Buy men's suits, sherwani & wedding ",
#                   "cover_image":"https://s-media-cache-ak0.pinimg.com/originals/bc/0a/6b/bc0a6bfd3855ebbe25b409df516287a9.jpg",
#                   "licence_no":"8"
#                 }
#         self.__store_service.register(store8)
#         
#         store9 = {
#                   "name":"raju",
#                   "street_address":"123-A, Rohini delhi",
#                   "postal_code":"110089",
#                   "city":"delhi",
#                   "country":"India",
#                   "contact_number":"8447673122",
#                   "description":"Shop for beautiful wedding wear online, designed by Manyavar, a leading celebration wear brand for men across India. Buy men's suits, sherwani & wedding ",
#                   "cover_image":"https://s-media-cache-ak0.pinimg.com/originals/bc/0a/6b/bc0a6bfd3855ebbe25b409df516287a9.jpg",
#                   "licence_no":"9"
#                 }
#         self.__store_service.register(store9)
#         
#         store10 = {
#                   "name":"nawaz",
#                   "street_address":"123-A, Rohini delhi",
#                   "postal_code":"110089",
#                   "city":"delhi",
#                   "country":"India",
#                   "contact_number":"8447673122",
#                   "description":"Shop for beautiful wedding wear online, designed by Manyavar, a leading celebration wear brand for men across India. Buy men's suits, sherwani & wedding ",
#                   "cover_image":"https://s-media-cache-ak0.pinimg.com/originals/bc/0a/6b/bc0a6bfd3855ebbe25b409df516287a9.jpg",
#                   "licence_no":"10"
#                 }
#         self.__store_service.register(store10)                
        
    
    def remove_data(self):
        return config.db.STORES.remove()
