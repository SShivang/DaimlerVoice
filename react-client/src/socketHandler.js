export function handle(state, action){
    console.log('Start action')
    console.log(action)
    if(action.view === 'action'){
        if(action.action === 'add_text'){
            const index = state.notes.length-1
            const note = state.notes[index]
            return {...state, notes: state.notes.slice(0, index).concat(note + " " + action.text)}
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
    else if(action.view === 'MAIN'){
        return handleMain(state, action)
    }
    else if(action.view === 'REPORT'){
        return handleReport(state,action)
    }
    else{
        console.log('NO HANDLER FOR ACTION ' + action.view)
    }
}

function handleMain(state, action){
    let newView = state.view[state.view.length-1] === action.view ? state.view : state.view.concat('MAIN')
    return {...state, view: newView}
}

function handleNote(state, action){
    console.log('handling note')
    let newView = state.view[state.view.length-1] === action.view ? state.view : state.view.concat('NOTE')
    return {...state, view: newView, notes: state.notes.concat(action.noteStr)}
}

function handleDiag(state, action){
    console.log('handling diag')
    let newView = state.view[state.view.length-1] === action.view ? state.view : state.view.concat('DIAG')
    return {...state, view: newView, step: action.text, table: (action.table === "YES"), 
        report: action.prev !== ''  && state.report[state.report.length-1] !== action.prev
        ? state.report.concat(action.prev) : state.report}
}

function handleReport(state, action){
    let newView = state.view[state.view.length-1] === action.view ? state.view : state.view.concat('REPORT')
    return {...state, view: newView}
}