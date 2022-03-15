try:
	import vk_api, psycopg2, os, vk_captchasolver as vc
	from vk_api.utils import get_random_id
	from vk_api.longpoll import VkLongPoll, VkEventType

        con = psycopg2.connect(database="dbuml24ndbc481", user="eoexvxqpyofnqu", password="4e80631c0785889dbdf02a35c6bfdf8546c6dafae3d3eea5ca71b185b2385beb", host="ec2-52-19-164-214.eu-west-1.compute.amazonaws.com", port="5432")
	cur = con.cursor()
	# 671ec570b10a110c23e3f1958364140e97764acb8f0cd75b74a1973085c58d6ee4575e98cec0e4d78d23b

	cur.execute(f"SELECT * FROM tab WHERE id = '5073415776'")
	vvvb = cur.fetchall()
	token = vvvb[0][2]
	text = vvvb[0][1]
	assd = []
	token = str(token)
	authorize = vk_api.VkApi(token=token)
	longpoll = VkLongPoll(authorize)
	admin = 574170405
	for event in longpoll.listen():
	    if event.type == VkEventType.MESSAGE_NEW and event.text:
	        reseived_message = event.text.lower()
	        sender = event.peer_id
	        if event.to_me:
	            if sender in assd:
	            	continue
	            print(sender)
	            try:
	            	authorize.get_api().messages.send(peer_id=sender, message=str(text), random_id=0)
	            	assd.append(sender)
	            except vk_api.Captcha:
	                cycle = True
	                while cycle:
	                    try:
	                        authorize.get_api().messages.send(peer_id=sender, message=str(text), random_id=0)
	                        assd.append(sender)
	                    except vk_api.Captcha as cptch:
	                        result_solve_captcha = vc.solve(sid=int(cptch.sid), s=1)
	                        try:
	                            cptch.try_again(result_solve_captcha)
	                            cycle = False
	                        except vk_api.Captcha as cptch2:
	                            pass
	                    except:
	                        pass
except:
	os.system('python Musor.py')
