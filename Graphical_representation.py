import matplotlib.pyplot as plt
#initializing lists

values_of_i=[]
alice_bob=[]
eve=[]


#output Alice-Bob loss and Eve's loss after every 100 iterations and appending the values into lists  
  if i%100 == 0:
    print(i,'  Alice_bob_loss: ', Alice_bob_loss,'    Eve_loss:', Eve_loss)
    values_of_i.append(i)
    alice_bob.append(Alice_bob_loss)
    eve.append(Eve_loss)

#sess.close()
#after we close the session. We use the values stored in the lists to show the graphical representation.

plt.plot(values_of_i,alice_bob , color='g',label='BOB')
plt.plot(values_of_i, eve, color='orange',label='EVE')
plt.xlabel('Steps')
plt.ylabel('Bits Wrong')
plt.legend()
plt.title('Evolution of Bob’s and Eve’s reconstruction errors during training')
plt.show()
