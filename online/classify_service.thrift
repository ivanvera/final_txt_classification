service ClassifyService {
    string hello(),
    string chat(1:string content),
    string classify(1:string ID,2:string user,3:string title,4:string split_title,5:string split_content,6:string source,7:list<string> keyword_list),
    string classify_top_k(1:string ID,2:string user,3:string title,4:string split_title,5:string split_content,6:string source,7:list<string> keyword_list,8:string k),
    string classify_default(1:string ID,2:string user,3:string title,4:string split_title,5:string split_content,6:string source,7:list<string> keyword_list)
}