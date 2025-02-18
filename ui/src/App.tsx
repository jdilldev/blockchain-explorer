import { useEffect, useState } from 'react'
import './App.css'
import axios from 'axios'

const App = () => {
  const [blockchainAddress, setBlockchainAddress] = useState('')
  const [balance, setBalance] = useState<string | undefined>(undefined)

  useEffect(() => {
    const getBalance = async (address: string) => {
      const res = await axios.get(`http://18.233.163.124:5000/address/balance/${address}`)
      setBalance(res['data']['balance'])
    }
    if (blockchainAddress)
      getBalance(blockchainAddress)
  }, [blockchainAddress])

  return (
    <div style={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      marginTop: '25%',
      color: 'white'
    }}>
      <label>Enter Blockchain Address</label>
      <input type='text' style={{ width: '70%' }} onChange={(e) => setBlockchainAddress(e.target.value)} />
      {balance && <p style={{ color: 'greenyellow' }}>{`Balance: ${balance}`}</p>}
    </div>
  )
}

export default App
