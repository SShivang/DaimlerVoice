export function handle(state, action){
    console.log('Start action')
    console.log(action)
    if(action.view === 'action'){
        if(action.action === 'add_text'){
            return {...state, noteStr: state.noteStr.concat(" " + action.text)}
        }
        else if(action.action === 'go_back'){
            return {...state, view: state.view.slice(0, state.view.length-1)}
        }
    }
    else if(action.view === 'NOTE'){
        return handleNote(state, action)
    }
    else if(action.view === 'DIAG'){
        return handleDiag(state, action)
    }
    else{
        console.log('NO HANDLER FOR ACTION ' + action.view)
    }
}

function handleNote(state, action){
    console.log('handling note')
    let newView = state.view[state.view.length-1] === action.view ? state.view : state.view.concat('NOTE')
    return {...state, view: newView, noteStr: action.noteStr}
}

function handleDiag(state, action){
    console.log('handling diag')
    let newView = state.view[state.view.length-1] === action.view ? state.view : state.view.concat('DIAG')
    return {...state, view: newView, step: action.text}


}