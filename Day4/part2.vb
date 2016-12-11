Module Day4

    Sub Main()
        Dim data As String = My.Computer.FileSystem.ReadAllText("data.txt")
        DoWork(data)
        Console.Read()
    End Sub

    Sub DoWork(data As String)
        Dim sum = 0
        Dim lines = data.Split(vbCrLf)
        For Each line In lines
            line = line.Trim()
            Dim lettersCount As New Dictionary(Of Char, Integer)

            Dim idx = line.LastIndexOf("-")
            Dim roomName = line.Substring(0, idx)
            Dim sectorIdAndChecksum = line.Substring(idx + 1)
            Dim lastSegment = sectorIdAndChecksum.Replace("]", String.Empty).Split("[")
            Dim sectorId = Convert.ToInt32(lastSegment.First())
            Dim checksum = lastSegment.Last()

            Dim shiftedRoomName = ShiftName(roomName, sectorId)

            If shiftedRoomName.Contains("northpole") Then
                Console.WriteLine($"{shiftedRoomName} : {sectorId}")
            End If  
        Next
    End Sub

    Function ShiftName(ByVal name As String, ByVal nbShifts As Integer) As String
        Dim result = String.Empty

        For Each c In name
            Dim charInt = Asc(c)

            If charInt >= Asc("a") AndAlso charInt <= Asc("z") Then
                charInt = charInt - Asc("a")
                charInt = (charInt + nbShifts) Mod 26
                result += Chr(charInt + Asc("a"))
            Else
                result += c
            End If            
        Next

        Return result
    End Function

End Module
