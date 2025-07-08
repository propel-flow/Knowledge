How did you load the whole code base into Claude for Work UI/Chat? - was that via Serena MCP?  
Can you send me the code & prompts you use for the i18n audit and code change? E.g. 
- The knowledge behind the i18n project  
- MCP server for adding Serena  
- Progress files - every time you update a file to be compatible (can start a new chat to repeat & continue)

Thanks so much - I want to leverage it for the Versioning control & changes in the UI work (for both Sree's team in product docs, and the translation UI human reviewers - so they can keep track of what actually to review).

---

Sure here is the serena MCP server - [https://github.com/oraios/serena](https://github.com/oraios/serena)   i added you the the i18n project so that you can look at my prompts... should be easy enough to follow [https://claude.ai/project/0197a233-75b9-72de-8ae1-e713dea12912](https://claude.ai/project/0197a233-75b9-72de-8ae1-e713dea12912)   this is the repo i was bringing in i18n support to - [https://github.com/extremenetworks/web-controller](https://github.com/extremenetworks/web-controller)

as long as you have git installed on your machine, claude can understand how to use it for comparing branches, diff etc.

just by talking to it...this will prompt serena to activate in the project....serena docs should give you more info on how it works