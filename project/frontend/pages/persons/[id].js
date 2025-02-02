import { useRouter } from 'next/router';
import { useEffect, useState } from 'react';
import { redirect } from 'next/navigation'


export default function Person()
{
    const [person, setPerson] = useState([]);

    const router = useRouter()
    const { id } = router.query

    useEffect(() => {
        if (id) {
          fetch(`https://jrappdev.onrender.com/persons/${id}`)
            .then((response) => {
              if (!response.ok) {
                router.push('/error')
                return null;
              }
              return response.json();
            })
            .then((data) => {
                if (data) {
                  setPerson(data);
                }
              })
              .catch((error) => {
                console.error("Error fetching person:", error);
                router.push('/error'); // Redirect if there is a fetch error
              });
        }
      }, [id]);

    return (
        <div className="flex flex-row p-8 justify-center align-center">
            <div className="bg-stone-100 rounded-lg p-4 text-center">
                <h1 className="font-sans text-3xl font-bold pb-3 text-slate-800">Jr. App Developer Project</h1>
                <h3 className="font-sans text-xl text-slate-800 ">Sathvik Parasa</h3>
                <h3 className="font-sans text-l text-slate-800 ">922076112</h3>
                <h3 className="font-sans text-l pb-2 text-slate-800 ">saparasa@ucdavis.edu</h3>

                <div className='font-sans text-m pb-4 text-slate-800'>
                    <h3 className="font-sans font-bold pb-2 text-xl pb text-slate-800 ">/persons/&lt;id&gt;</h3>
                    <p>Fetch the details of the UUID:</p>
                    <p className='pb-2'>{id}</p>

                    <ul className="space-y-2">
                    <li
                        key={person.Id}
                        className="p-4 bg-white shadow rounded-lg flex justify-between items-center">
                        <div>
                        <p className="font-bold text-stone-800">
                            {person.First_Name} {person.Last_Name}
                        </p>
                        <p className='text-xs text-stone-600 text-end'>{person.Id}</p>
                        <p className="text-stone-600">{person.Email}</p>
                        </div>
                        <p className="text-stone-800 font-semibold">${person.Salary}</p>
                    </li>
                </ul>
                </div>
                
                <a className="bg-stone-800 mb-3 hover:bg-stone-950 text-white font-bold py-2 px-4 mr-2 rounded" href='/'> Go to /</a>
                <a className="bg-stone-800 hover:bg-stone-950 text-white font-bold py-2 px-4 rounded" href='/persons'> Go to /persons</a>
            </div>
        </div>
    )
}