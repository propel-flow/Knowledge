
# Product Requirements Document: Claude Integration for Technical Writing Teams

## Executive Summary

Based on feedback from Sreeranjani Pattabiraman (Technical Writing team), this PRD outlines the pain points, successful use cases, and feature requirements for Claude integration within technical documentation workflows.

## Current Pain Points & Challenges

### 1. **Rate Limiting & Capacity Constraints**

- **Problem**: Users frequently hit daily usage limits, receiving messages like "I've hit the limit for the day and my chat will be reset at 6:00 PM Eastern Time"
- **Impact**: Blocks productivity when testing multiple use cases simultaneously (7-8 different use cases running concurrently)
- **Current Workaround**: Manual queue management and telling team members to "slow things down"
- **Status**: Will be resolved with enterprise licensing

### 2. **Session Timeouts & Performance Issues**

- **Problem**: Claude frequently times out when running multiple processes simultaneously
- **Contributing Factors**: Running 12 different tasks concurrently
- **Impact**: Workflow interruptions and reduced efficiency

### 3. **Missing Nuanced Information**

- **Problem**: Claude provides good "non-halo synthetic versions" of topics but misses nuanced information that technical writers typically gather from SME interviews
- **Gap**: Complex documentation requirements that need deep subject matter expertise
- **Current Solution**: Technical writers still need to conduct SME interviews and research to fill gaps

### 4. **Data Access Limitations**

- **Problem**: Cannot access website metrics for PDFs and other documentation formats
- **Impact**: Unable to test content audit and analytics use cases effectively
- **Dependency**: Waiting for HTML transition to get better statistics

### 5. **MCP & Integration Challenges**

- **Problem**: Waiting for InfoSec approval for MCP implementations
- **Current Status**: Multiple MCP projects in development queue (3-4 simultaneously)
- **Workaround**: Exploring local HTML downloads as proof of concept

## Successful Use Cases & Features

### 1. **Screenshot Documentation & Analysis**

**Feature**: Built-in screenshot capability within chat window (Opus 4)

- **Use Case**: Documenting simple UI screenshots effectively
- **Success**: Provides good baseline documentation that technical writers can refine
- **Enhancement Opportunity**: Technical writer expertise needed for proper screenshot framing and context

**Feature**: Screenshot comparison and gap analysis

- **Use Case**: Comparing existing documented screens with new versions
- **Output**: Identifies major differences and missing information
- **Value**: Reduces manual comparison time

### 2. **Content Strategy & Document Planning**

**Feature**: Strategic document planning assistance

- **Use Case**: Deciding whether to create separate documents or merge existing ones
- **Time Savings**: "Typically my team would spend hours doing that research"
- **Impact**: Significant reduction in strategic planning time

### 3. **Artifact Editing & Improvement**

**Feature**: In-line editing within the editorial window

- **Functionality**:
    - "Improve" option with description input for content enhancement
    - "Explain" option for detailed reasoning behind changes
- **User Feedback**: "I thought that was a cool functionality"

### 4. **Document Generation from Existing Content**

**Feature**: Full document creation from reference materials

- **Use Case**: Generated 30-page first draft using:
    - Older unsupported document as reference
    - Functional specifications for new product
- **Next Steps**: End-to-end review by technical writers planned for accuracy validation

### 5. **PRD Generation**

**Feature**: Product Requirements Document creation

- **Use Cases**:
    - Internal PRDs for team processes
    - External PRDs for vendor communications
    - PLM team documentation for document retention decisions
- **Integration**: Plans to combine with content audit data for enhanced metrics

## Planned Integrations & Advanced Features

### 1. **CCMS Integration Layer**

- **Objective**: Building communication layer on top of CCMS (similar to MCP approach)
- **Status**: In development with Kira
- **Expected Value**: Streamlined content management workflow

### 2. **Translation Capabilities**

- **Current Approach**: Testing translation of phrases in five different languages
- **Challenge**: Claude alone lacks sophisticated glossary and product name mapping
- **Solution**: Requires backend glossary integration with keyword mapping and human reviewer learnings

### 3. **Content Audit & Analytics**

- **Planned Feature**: Metrics-driven content decisions
- **Dependency**: Website metrics access (currently unavailable for PDFs)
- **Integration**: Combining with PRD generation for weighted decision-making

## Training & Best Practices Requirements

### 1. **Prompt Engineering Training**

**Need**: Team training on effective Claude interaction

- **Focus Areas**:
    - Question formulation best practices
    - Understanding what works better than alternatives
    - Technical writing-specific prompting strategies

### 2. **Use Case Documentation**

**Requirement**: Document successful patterns and failure modes

- **Purpose**: Enable team scaling when enterprise access is available
- **Content**: What works well vs. what doesn't, with specific examples

## Technical Infrastructure Needs

### 1. **Enterprise Access**

- **Current Blocker**: Individual usage limits preventing team scaling
- **Required**: Enterprise licensing to support multiple concurrent users

### 2. **MCP Development Priority**

- **Current Queue**: 3-4 MCPs in development
- **Specific Need**: WS2 instance screenshot integration
- **Alternative**: Local HTML download for proof of concept

### 3. **Data Integration**

- **Missing**: Website analytics for existing PDF documentation
- **Future**: HTML transition will enable better statistics collection

## Success Metrics & Validation

### 1. **Immediate Validation Planned**

- **30-page document review**: Technical writers will conduct end-to-end accuracy review
- **Manual process comparison**: Measuring accuracy against traditional methods

### 2. **Time Savings Achieved**

- **Strategic planning**: Hours of research time reduced to minutes
- **Screenshot documentation**: Faster baseline creation with expert refinement

### 3. **Quality Assessment**

- **Simple tasks**: "Pretty good job" with basic UI documentation
- **Complex tasks**: Requires technical writer intervention for nuanced information

## Recommendations

### 1. **Immediate Actions**

- Prioritize enterprise licensing to remove usage constraints
- Accelerate MCP development for screenshot integration
- Document successful prompt patterns for team training

### 2. **Medium-term Development**

- Integrate translation capabilities with existing glossary systems
- Develop CCMS communication layer
- Enable website analytics access for content audit capabilities

### 3. **Long-term Strategy**

- Scale team adoption based on documented best practices
- Integrate content audit data with PRD generation
- Establish metrics-driven content decision framework

This PRD reflects a technical writing team already achieving significant productivity gains while identifying clear paths for enhanced functionality and team scaling.
---


## **Transcript** 
June 12, 2025, 5:41PM ![](media/image1.png){width="0.22916666666666666in" height="0.22916666666666666in"}**\ Katie Potter** started transcription ![](media/image2.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Sreeranjani Pattabiraman** 0:03\ We were doing with copilot Taurus able to provide a good. ![](media/image3.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Katie Potter** 0:05\ Mm hmm. ![](media/image2.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Sreeranjani Pattabiraman** 0:09\ Non Halo synthetic version.\ Of the topic.\ But if we give it a very complex one, of course it misses the nuances, which is expected, because that information is what tech writers on my team would have.\ And that\'s where they would come in to fix that.\ But it it\'s been doing.\ I wanna say a pretty good job with documenting.\ Simple UI screenshots and I also feel that\'s where the tech writers expertise would come in, framing the screenshots a certain way and taking it in a certain way to make sure that a cloud is able to take that and one of the other things you people may have.\ Already noticed it, but Claude has an inbuilt capability to take screenshots too. ![](media/image3.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Katie Potter** 0:59\ OK, interesting. I wonder how. ![](media/image2.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Sreeranjani Pattabiraman** 0:59\ Like within the within the chat window itself, I\'m using Office 4, so within the chat window itself you have an option to take a screenshot. ![](media/image3.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Katie Potter** 1:10\ Can can you send me the WS2 or whichever instance you\'re using to take your screenshots in? I wanna do a test if I can download it locally and maybe we can run an MCP locally. ![](media/image4.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Tuba Hashmi (CW)** 1:10\ All right. ![](media/image2.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Sreeranjani Pattabiraman** 1:24\ Yeah. So that, yeah, if we can do that, I that\'s one of the things that Kira and I are exploring too.\ The MCP for doing that, but yeah, I can give you the login credentials for WS2. ![](media/image3.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Katie Potter** 1:36\ Yeah. Give me those. Just to remind me, I again, I\'m trying to do like three or four MCPS at the moment. So I don\'t know how quickly I\'m gonna get through them all, but if I can download that HTML locally, I might be able to get you at. ![](media/image2.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Sreeranjani Pattabiraman** 1:44\ Mm hmm. ![](media/image3.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Katie Potter** 1:49\ Least a proof of concept of that sooner than waiting for info SEC. ![](media/image2.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Sreeranjani Pattabiraman** 1:53\ Yeah.\ And then the other thing is also I so I I\'m using it for strategizing.\ So we have a lot of requests for creating new docs so.\ Really helping it build a strategy around if it would make sense to keep the doc separated or if it would make sense to merge them together. Things like that.\ Typically my team we would spend hours doing that research, so it cuts down a lot of our time doing things like that. ![](media/image3.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Katie Potter** 2:18\ Mm hmm. ![](media/image2.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Sreeranjani Pattabiraman** 2:25\ So it\'s been particularly.\ Helpful for that. ![](media/image3.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Katie Potter** 2:28\ Oh, that\'s really great. ![](media/image2.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Sreeranjani Pattabiraman** 2:29\ And yeah. ![](media/image3.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Katie Potter** 2:29\ Can you share that conversation with me? ![](media/image2.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Sreeranjani Pattabiraman** 2:32\ Yeah, sure.\ I can do that.\ And then the other use case where one of the other things related to screenshot that I was able to test out was since some of the screens are already documented, I was able to give the information of what was documented and use Claude to let me know what.\ The major difference is and what information is missing from what it it is developing and what I realized was it\'s usually the nuanced information.\ That tech writers get directly from SMEs, or that\'s where we need to do the whole.\ You know, whole research and SME interview type things the other. ![](media/image3.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Katie Potter** 3:15\ And and that\'s where I think the power of those demos that we were talking about like a couple months ago now would come in, right? ![](media/image2.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Sreeranjani Pattabiraman** 3:19\ Yes.\ Yeah. ![](media/image3.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Katie Potter** 3:22\ I wonder if there\'s some recordings or you can get some of your team to retest recordings in certain ways to get the missing information that you notice is coming through and then we can pair that in with additional context as well. ![](media/image2.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Sreeranjani Pattabiraman** 3:33\ Mm H.\ Yes, I agree.\ The other thing that I noticed was if you were to.\ So what are the results that Claude gives?\ And if you were to improve it, or if you were to ask it to explain it, you can do that within the editorial window itself.\ Have people tried that out?\ I thought that was a cool functionality. ![](media/image3.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Katie Potter** 3:59\ Can you show what you mean on screen? ![](media/image2.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Sreeranjani Pattabiraman** 4:02\ Let me see.\ I have to have let me find a chat in which.\ You should be able to see my screen.\ So say for instance I\'m asking it to change this. There\'s an option where I can say improve and then if I want to improve this I can describe it and it would update that and then if I wanted to explain then it would give me the results of.\ That. ![](media/image3.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Katie Potter** 4:44\ Wow, really cool. ![](media/image2.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Sreeranjani Pattabiraman** 4:45\ Yeah. Yeah, it is.\ One of the other things that I noticed was also I don\'t if it\'s because I\'m running 12 different things at the same time.\ It often times out on me, or if it or it sometimes tells me that I have hit the capacity or the limit.\ Yesterday I got a particularly interesting message that I have not seen before.\ This was later in my afternoon, so I was almost done running my testing and stuff.\ It said I\'ve been. I\'ve hit the limit for the day and then my.\ Chat will be reset at 6:00 PM Eastern Time for me to do carry on with more testing. ![](media/image3.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Katie Potter** 5:24\ We\'ll get over that with enterprise, but I love that you\'re coming into the same problem because I am too. ![](media/image2.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Sreeranjani Pattabiraman** 5:26\ Yes, exactly. ![](media/image3.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Katie Potter** 5:29\ I\'m like, why am I impatient now with AI?\ Because I\'m setting up four windows of AI at once, trying to get it. ![](media/image2.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Sreeranjani Pattabiraman** 5:35\ Yes, I mean I can tell you right now.\ I have probably you know 7 to 8 different use cases running at the same time and as and when my team reaches out to me, I\'m like, OK, let me run this. ![](media/image3.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Katie Potter** 5:44\ Yeah. ![](media/image2.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Sreeranjani Pattabiraman** 5:48\ So I add on to the queue. So as I have to tell people like, OK, you, you may have to slow things down because I\'m not able to do it fast enough, even though it\'s, you know, faster than anything we have. ![](media/image3.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Katie Potter** 6:00\ I know if we\'ve ever done before, it\'s crazy. ![](media/image2.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Sreeranjani Pattabiraman** 6:03\ Yes. ![](media/image3.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Katie Potter** 6:03\ But now our expectation is just like 10 \* 10 in terms of what\'s possible. ![](media/image2.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Sreeranjani Pattabiraman** 6:08\ Yeah. ![](media/image3.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Katie Potter** 6:08\ So I think what would be useful as well, Sree, is to start documenting the things that work really well and and don\'t so that you can start to think about how you\'d train your team like we\'re going to overcome these roadblocks of you having seven open in the. ![](media/image2.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Sreeranjani Pattabiraman** 6:17\ Mm hmm. ![](media/image3.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Katie Potter** 6:21\ Future, once they all get it right. What are the things that are important to help them learn how to use it successfully? ![](media/image2.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Sreeranjani Pattabiraman** 6:23\ Yeah, yeah.\ Yes. Yeah. And I think also from my team\'s perspective, one thing that I have been thinking about is providing training on prompt engineering and just making sure that from a tech writing standpoint, best practices establishing that, that will be so helpful for writers in understanding what sort.\ Of questions.\ Are you supposed to ask what will work better than other and I?\ I already have some use cases for that, but I I\'m going to build on it.\ Another interesting thing.\ In that, Kira and I are working on are basically.\ I\'m also making it similar to what you\'re doing with MCP.\ I\'m also like trying to do that from a CCMS standpoint, building a layer on top of that and establishing that communication layer.\ But I\'m also helping it build prds for me both internally and externally. If we were to talk to vendors about wanting a functionality and also within our PLM team to.\ To give more weightage to reasoning for keeping a document or not keeping something.\ But I think combining that with the content audit that we\'re doing on the side and having more data feeding that that will really help us with metrics and other things too.\ I haven\'t really had a chance to explore it just because I don\'t have the data set for it, but that\'s another use case that I want to test out from my team\'s perspective. ![](media/image3.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Katie Potter** 7:56\ Yeah, and and what is that data set exactly that you would need to run that test successfully? ![](media/image2.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Sreeranjani Pattabiraman** 8:03\ So it\'s the metrics that we get from our website, which we don\'t, which is not right now. There are no metrics on PDFs and stuff.\ So it it will be whatever data I use for testing will be.\ Not not a good data set in my opinion. ![](media/image3.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Katie Potter** 8:20\ OK, right.\ Well, that\'s, that\'s another thing that we can as soon as we shift to our HTML piece get much better statistics off of that as well.\ So I guess that\'s just another reason for us to switch. ![](media/image2.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Sreeranjani Pattabiraman** 8:31\ Yeah. ![](media/image3.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Katie Potter** 8:34\ But yeah, anyway I I won\'t push that agenda.\ It\'s going to happen when it\'s going to happen and I think things are moving so quickly that it\'s probably going to happen.\ Sooner rather than later. ![](media/image2.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Sreeranjani Pattabiraman** 8:48\ Yeah, but so far really good.\ Good use cases that I got from my team and I\'ve been I also actually made it build a document based on one of the existing documents that we have which we don\'t support anymore.\ But then we have a newer product for which we we got a request to build something similar.\ So I gave it the older doc and I told it to.\ I also gave the functional specs for the newer DOC and I told it to build it and it was able to build a 30 page first draft.\ So next week I\'m going to ask the writers on it to do an end to end review of it.\ And then do do a manual process to see how far accurate that information is. ![](media/image3.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Katie Potter** 9:37\ Was there any action item from me on that or was that just chairing back? ![](media/image2.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Sreeranjani Pattabiraman** 9:41\ No, that just sharing feedback on that. ![](media/image3.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Katie Potter** 9:43\ Yeah, OK, good to good to know. Yeah, I mean. ![](media/image2.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Sreeranjani Pattabiraman** 9:46\ I had. Yeah, go ahead. ![](media/image3.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Katie Potter** 9:48\ You go.\ No, no. I was just going to say it\'s great. ![](media/image2.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Sreeranjani Pattabiraman** 9:51\ Yeah, I did have a question around translations.\ I I know that your team is doing the translation tool, but I did want to test out translation too.\ So are you all using cloud for that or would it be better for me to give some testing material to you?\ To test in your tool. ![](media/image3.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Katie Potter** 10:13\ Material because we\'ve tested on Claude originally and we know Claude is good.\ Claude\'s expensive though.\ So when we do it at scale, we actually pair back to a different model.\ That\'s just as effective.\ And what actually makes it effective is the way that we train the AI.\ It doesn\'t matter which AI it is, it\'s what we send it in the prompt window.\ So we actually have a sophisticated glossary in the back end that. ![](media/image2.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Sreeranjani Pattabiraman** 10:36\ Mm hmm. ![](media/image3.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Katie Potter** 10:38\ Maps keywords that we\'ve learnt from human reviewers over time and also has our full list of product names.\ In there and Claude wouldn\'t get that just by you putting in the interface.\ So yeah, we\'re going to have to run those tests on our end. ![](media/image2.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Sreeranjani Pattabiraman** 10:50\ Mm hmm.\ OK, OK.\ I\'ll I\'ll send you some.\ I have actually just a couple of phrases that need to be translated in five different languages. ![](media/image3.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Katie Potter** 11:03\ Mm hmm. ![](media/image2.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Sreeranjani Pattabiraman** 11:03\ So I\'ll I\'ll send that. Send those over to you.\ So you should be able to test it and.\ And we can include that in our.\ It\'s for the quick reference guide so we can do that. ![](media/image3.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Katie Potter** 11:17\ OK, sounds good.\ Anything else from anyone else here, marooq.\ Anything from your end, Brian from your end. ![](media/image5.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Brian Herzfeldt** 11:29\ I had a question on when you\'re you\'re creating like graphics or interfaces.\ Like I create an interface.\ Couple of them, several of them and it gives me like the home page and you can click on things, but it just gives me a link to another prompt page. If I click on them.\ Is that normal? ![](media/image3.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Katie Potter** 11:48\ I would ask Ryan more about that.\ I think he knows more of the capability from a design point of view.\ I think he touched on that in our design, Claude for design session we had on Wednesday.\ I just can\'t remember exactly what he said.\ So you can follow up in that Claude for design chat and see.\ See what he comes up with there. But also I know that once we get this figma MCP connection going, that that\'s kind of going to leverage that on steroids too.\ I just don\'t know what the workflow transition is from doing it in Claude to doing it in figma. ![](media/image5.png){width="0.3020833333333333in" height="0.3020833333333333in"}**\ Brian Herzfeldt** 12:24\ Yeah, I talked to Ron Ronald yesterday about that.\ I had a meeting with him and we talked about some stuff.