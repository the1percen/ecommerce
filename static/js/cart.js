var updatebuttons = document.getElementsByClassName('update-cart')

for(i = 0; i < updatebuttons.length; i++){
    updatebuttons[i].addEventListener('click', function(){
        var productID = this.dataset.product
        var action = this.dataset.action
        console.log('productID:', productID, 'Action: ', action )

        console.log('USER: ', user)
        if(user == 'AnonymousUser'){
            console.log('User is invalid')
        }else{
            console.log('user is authenticated, sending data.....' )
        }
    })
}