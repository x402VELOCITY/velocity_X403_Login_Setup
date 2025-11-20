import { useState, useEffect } from 'react';
import { OpenKit403Client, detectWallets } from '@openkitx403/client';
import { useRouter } from 'next/navigation';

function CApp() {
    const [client] = useState(() => new OpenKit403Client());
    const [wallets, setWallets] = useState([]);
    const [address, setAddress] = useState(null);
    const router = useRouter();

    useEffect(() => {
    detectWallets().then(setWallets);
    }, []);

    const authenticate = async (wallet) => {
        await client.connect(wallet);
        const response = await client.authenticate({
            resource: '[velocityurl]/accountlogin'
        });


        if (response.ok) {
            const data = await response.json();
            setAddress(client.getAddress());
            localStorage.setItem("loadedwallet",client.getAddress())
            alert('✅ Authenticated successfully!');
            router.push('/dashboard');

        } else {
            alert('❌ Failed: ' + response.status);
        }
    };

    return (
        <div>
            <h1>X403</h1>
            {address ? (
                <p>✅ Connected as: {address}</p>
                ) : (
                wallets.map(wallet => (
                <button key={wallet} onClick={() => authenticate(wallet)}
                 className="text-bg text-mono bg-rose-500/10 text-rose-300 hover:bg-rose-500/20 w-full"
                
                >
                    Connect {wallet}
                </button>
                ))
            )}
        </div>
    );
}

export default CApp;
