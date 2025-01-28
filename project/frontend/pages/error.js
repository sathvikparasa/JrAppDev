export default function Error() {  
  return (
    <div className="flex flex-row p-8 justify-center align-center">
      <div className="bg-stone-100 rounded-lg p-4 text-center">
        <h1 className="font-sans text-3xl font-bold pb-3 text-slate-800 ">Jr. App Developer Project</h1>
        <h3 className="font-sans text-xl text-slate-800 ">Sathvik Parasa</h3>
        <h3 className="font-sans text-l pb text-slate-800 ">922076112</h3>
        <h3 className="font-sans text-l text-slate-800 ">saparasa@ucdavis.edu</h3>
        
        <h1 className="font-sans pt-3 pb-4 font-bold text-xl text-slate-800">Oops! Something went wrong...</h1>
        <a className="bg-stone-800 hover:bg-stone-950 text-white font-bold py-2 px-4 rounded" href='/'>Go back to home</a>
      </div>
    </div>
  )
}