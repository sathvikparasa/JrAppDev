import { useEffect, useState } from 'react';
import { redirect } from 'next/navigation'
import Link from "next/link";

export default function Persons() {
    const [persons, setPersons] = useState([]);

    useEffect(() => {
        fetch("https://jrappdev.onrender.com/persons")
        .then((response) => {
            if (!response.ok) {
              redirect("/error")
            }
            return response.json();
          })
          .then((data) => {
            setPersons(data);
            // setLoading(false);
          })
          .catch((error) => console.error("Error fetching persons:", error));
      }, []);

    return (
        <div className="flex flex-row p-8 justify-center align-center">
            <div className="bg-stone-100 rounded-lg p-4 text-center">
                <h1 className="font-sans text-3xl font-bold pb-3 text-slate-800 ">Jr. App Developer Project</h1>
                <h3 className="font-sans font-bold text-xl pb text-slate-800 ">/persons</h3>
                <p className="font-sans text-m pb-4 text-slate-800">Fetch the details of the first 10 people from persons.csv</p>
                <ul className="space-y-2 pb-4">
                    {persons.map((person) => (
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
                    ))}
                </ul>

                <a className="bg-stone-800 hover:bg-stone-950 text-white font-bold py-2 px-4 rounded" href='/'>Go back</a>
            </div>
        </div>
    );
}