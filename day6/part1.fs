open System
open System.IO

let mergeCharArrayToString (xs : char list) : string =
    let sb = System.Text.StringBuilder(xs.Length)
    xs |> List.iter (sb.Append >> ignore)
    sb.ToString()

let findMostCommonLetter (elems : char list) : char = 
    fst (elems 
            |> List.groupBy (fun c -> c) 
            |> List.sortByDescending (fun t -> Seq.length (snd t))
        ).[0]    

let rec groupLettersByPosition (data: char list []) (index: int) (acc: char list list) : char list list =
    if index = data.[0].Length then
        acc
    else
        let chars = Array.toList (Array.map (fun (s : char list) -> s.[index]) data)
        let nextAcc = List.append acc [chars]
        groupLettersByPosition data (index + 1) nextAcc    

[<EntryPoint>]
let main argv = 
    let rawData = Array.map (fun elem -> [for c in elem -> c]) (File.ReadAllLines("data.txt"))
    groupLettersByPosition rawData 0 []
        |> List.map (fun e -> findMostCommonLetter e)
        |> mergeCharArrayToString
        |> printfn "%A"

    Console.ReadKey() |> ignore
    0