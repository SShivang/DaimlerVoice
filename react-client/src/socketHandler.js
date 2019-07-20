export function handle(state, action){
    if(action.view =='NOTE'){
        return handleNote(state, action)
    }
    else{
        console.log('NO HANDLER FOR ACTION ' + action.view)
    }
}

function handleNote(state, action){
    console.log('handling note')
    return {...state, view: 'NOTE', noteStr: action.noteStr}
}