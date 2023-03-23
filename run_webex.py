import asyncio
from webex import App

app = App()
payload_create_room = {
    "title": "Imperum room",
    }
result=asyncio.run(app.create_room(payload=payload_create_room))



#roomId string olarak gonderilecek ve url kisminda yer alacak stringimiz
payload_get_room_details = {'roomId': 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vNjE3MmM2MzAtYjc0ZC0xMWVkLWIxM2QtYzdhMjNiZjQ5MWNj'}
result=asyncio.run(app.get_room_details(payload=payload_get_room_details))



payload_create_team = {
        'name' : 'Test123 Teams'
    }
result=asyncio.run(app.create_team(payload=payload_create_team))


#silmek istedigimiz teamin ,teamId'sini vererek
payload_delete_team ={'teamId' : 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1RFQU0vY2I4NDk1ZjAtYjc2NC0xMWVkLWJmYzYtN2JmYjk3OTMyNzQ2'}
result=asyncio.run(app.delete_team(payload=payload_delete_team))



#get list teamden team id'yi alip asagida kullaniyoruz
#'teamId' : 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1RFQU0vZDkxZDc2NDAtYjc2NS0xMWVkLWIwNzctMWRmNjVhOGMyMTI5',
#hangi teame uye eklmek istiyoruz Team id bundan dolayi zorunlu ve personEmaili girerek eklemeyi gerceklestiriyoruz
payload_create_memberships = {
        'teamId' : 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vYTIyMjljMzAtYjc0Zi0xMWVkLWI4NTAtZmY3OWFjYjEwNzhi',
        'personEmail' : 'test123@gmail.com'
    }
result=asyncio.run(app.create_memberships(payload=payload_create_memberships))



# yukaridan gelen team id'yi burada vermemiz gerekiyor bunun sonunucunda personal id alacagiz ve bunu da asagida ki details fonksiyonuna verecegiz
payload_get_list_team_memberships = {
        'teamId' : 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1RFQU0vZDkxZDc2NDAtYjc2NS0xMWVkLWIwNzctMWRmNjVhOGMyMTI5'
    }
result=asyncio.run(app.get_list_team_memberships(payload=payload_get_list_team_memberships))


#personal id
payload_get_team_membership_details ={'membershipId' : 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1RFQU1fTUVNQkVSU0hJUC84NzBkNzI3Yi1hMjQ0LTQ2MzctOTU0OC0wZjZmNjI2YTZiNzM6ZDkxZDc2NDAtYjc2NS0xMWVkLWIwNzctMWRmNjVhOGMyMTI5'}
result=asyncio.run(app.get_team_membership_details(payload=payload_get_team_membership_details))




#room id  onu da get_roomdan alabiliriz
payload_send_message= {
        'roomId' : 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vYTIyMjljMzAtYjc0Zi0xMWVkLWI4NTAtZmY3OWFjYjEwNzhi',
        'text' : 'test denemesi'
        }