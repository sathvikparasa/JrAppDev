// import Link from "next/link";
import { useState } from "react";
import Router, { useRouter } from "next/router";
// import { redirect } from 'next/navigation'


export default function Home() {  
  const [uuid, setUuid] = useState('')
  const router = useRouter()

  const handleSubmit = (e) => {
    e.preventDefault()
    if (uuid) {
      router.push(`/persons/${uuid}`)
    } else {
      alert('Please enter a valid UUID')
    }
  };

  return (
    <div className="flex flex-row p-8 justify-center align-center">
      <div className="bg-stone-100 rounded-lg p-4 text-center">
        <h1 className="font-sans text-3xl font-bold pb-3 text-slate-800 ">Jr. App Developer Project</h1>
        <h3 className="font-sans text-xl text-slate-800 ">Sathvik Parasa</h3>
        <h3 className="font-sans text-l pb text-slate-800 ">922076112</h3>
        <h3 className="font-sans text-l text-slate-800 ">saparasa@ucdavis.edu</h3>
        
        <form onSubmit={handleSubmit} className="flex-row mt-3 mb-4 text-center">
          <input className="text-center shadow appearance-none border rounded py-2 px-3 text-stone-700  focus:outline-none focus:shadow-outline" id="user_id" type="text" placeholder="Enter a UUID" onChange={(e) => setUuid(e.target.value)}/>
          <button type="submit" className="bg-green-800 hover:bg-green-950 text-white font-bold py-2 px-4 ml-2 rounded">Go</button>
        </form>
        <a className="bg-stone-800 hover:bg-stone-950 text-white font-bold py-2 px-4 rounded" href='/persons'>Fetch first 10 values</a>
      </div>
    </div>
  )
}