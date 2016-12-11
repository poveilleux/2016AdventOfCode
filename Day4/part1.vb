Module Module1

    Sub Main()
        Dim data As String = My.Computer.FileSystem.ReadAllText("data.txt")
        DoWork(data)
        Console.Read()
    End Sub

    Sub DoWork(data As String)
        Dim sum = 0
        Dim lines = data.Split(vbCrLf)
        For Each line In lines
            Dim sectorId As Integer
            Dim checksum As String
            Dim lettersCount As New Dictionary(Of Char, Integer)

            Dim segments = line.Trim().Split("-")
            Dim lastIndex = segments.Length - 1

            For i = 0 To lastIndex - 1
                For Each c In segments(i)
                    Dim count As Integer
                    If Not lettersCount.TryGetValue(c, count) Then
                        count = 0
                    End If
                    lettersCount(c) = count + 1
                Next
            Next
            
            Dim lastSegment = segments(lastIndex).Replace("]", String.Empty).Split("[")
            sectorId = Convert.ToInt32(lastSegment.First())
            checksum = lastSegment.Last()

            Dim calculatedChecksum = String.Join("", lettersCount.OrderByDescending(Function(pair) pair.Value).ThenBy(Function(pair) pair.Key).Select(Function(pair) pair.Key).Take(5))

            If calculatedChecksum = checksum Then
                sum += sectorId
            End If            
        Next 

        Console.WriteLine(sum)
    End Sub

End Module
