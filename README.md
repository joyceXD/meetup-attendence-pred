## Meetup prediction assignment

### Context: meetup.com
[Meetup.com](http://www.meetup.com) is a popular online platform with the aim of bringing together people with a shared interest in real-life events (meetups). The meetup community is composed of groups, where each group has a particular interest and organises events. Users of meetup.com can become member of one or more groups. Whenever a group organises an event, members of that group have the opportunity to RSVP for an event (yes, we're using RSVP as a verb here). The RSVP for an event can be either a Yes or No answer, meaning respectively that the member is either planning to attend the event or is not. Not RSVP-ing to an event can be interpreted as a No. Additionally, groups express the interests that they ostensibly have in terms of a number of topics (e.g. the [Spiritual Psychology Meetup](http://www.meetup.com/Spiritual-Psychology-Meetup/) has listed as topics: Philosophy, Self Exploration, Transformation, Meditation, etc.).

In summary, the essential entities and relations in the meetup.com ecosystem are:

- Users can join groups (becoming members)
- Groups have an organiser
- Groups discuss a set of topics
- Groups organise events
- Members can RSVP to events (Yes or No)
- An event is hosted at a venue

Apart from these basics, both groups, users, members, events and venues have particular metadata. You'll want to do some exploration of your own.

#### Tech Meetups
A special case of meetup events are what we call tech meetups. These are events focussing on technology (usually Information Technology / software engineering / computer science), with a typical conference style setup, where there are presentations and the members that attend are audience. Tech meetups are generally organised with the goal of knowledge sharing within the professional IT community. However, since these events are often attended by individuals with relevant and sometimes scarce skills in what are considered cutting edge technologies, these events are also popular targets for sponsorships from organisation who are actively hiring software engineers or data scientists.

This assignment will be about tech meetups.

### Assignment

The assignment is to create a model that can predict for a new, to be organised, meetup event how many members will RSVP to that meetup. This is useful for organisers to investigate whether minor changes to their event (e.g. event date / day of week) will have a positive influence on the number of expected attendees.

We expect you to spend no more than a couple of evenings (8 - 16h in total) on this assessment, as guideline we provide you with an expected effort in percentage on the required solutions below.

#### Required solution

##### 1. Predictive model (80%)
We expect you to provide us with a code that we can use to generate predictions for new meetup events. Your code should be organized so that, if we were to deploy it in a production system, we would not have to re-architecture it.

##### 3. Presentation (20%)
See Evaluation below for the expectations of this presentation.

##### Non (core-)functional requirements

- Your solution must work out-of-the-box. This means that an individual reasonably proficient with computers and programming should be able to get it running without having to contact you. A useful README must be in place if this is needed to meet this requirement.
- Your solution must run on Linux or Apple OS X. A solution that only runs on Microsoft Windows is not acceptable (this is for practical reasons; we hold nothing against Microsoft operating systems).
- Reasonable external dependencies are no problem. E.g. presence of a JVM or a simple to install database server. State these requirements in the README. If you are in doubt about whether we will get the solution to run, you could also deliver a virtual machine image that works for sure.
- It must be possible to change the data set. Provide some kind of documented way to do this. It is OK to require a restart of the service to do this.

##### Languages / frameworks / tools
There are no strict rules regarding choice of programming languages, (web) frameworks or tools. We value evidence of good software engineering practice. Things like automation, separation of concerns, testability, etc. We are not religious about any certain technology. Mixing of languages and tools where it makes sense is rather encouraged over forcing everything onto a single technology. You get the point. We want to see that you are capable of building a (simple) product, end-to-end.

### Data
For this assignment you will receive data for all meetup groups in the technology category within an area spanning a large part of The Netherlands, Belgium and some part of Germany (roughly all groups within a 100 mile radius from Amsterdam). The data contains information on groups, users, group membership, events and event RSVPs. Data is delivered in a number of separate files containing a single JSON blob of encoded arrays.

The following files will be provided:

- groups.json: An array containing all groups, including metadata and topics that apply to a group.
- users.json:  An array containing all users in the database, including metadata. All group memberships are contained in the user object.
- events.json: An array containing all meetup events, including metadata and RSVPs.
- venues.json: An array containing details about all venues referenced from the events data.

#### Groups
Each group object has the following fields:

- city: Name of the city where the group resides.
- created: Timestamp of when the group was created.
- description: Description of the group.
- name: Name of the group.
- lat: Lattitude of the place where the group resides.
- lon: Longitude of the place where the group resides.
- link: Link to the group's homepage.
- group_id: Unique identifier for this group. This is used as a reference in other objects.
- topics: Array of topics that this group discusses or otherwise associates with.

#### Users
Each user object has the following fields:

- user_id: A unique identifier for this user. Note that this identifier has no relation to internal identifiers from meetup.com; users can not be associated with actual accounts using this dataset. Such is for privacy reasons.
- city: City where the user resides.
- country: Country where the user resides.
- hometown: Town that the user specified as their home town.
- memberships: Array of membership objects, containing the following fields:
    - joined: Timestamp of the moment the user joined this group.
    - group_id: The unique identifier of the group that the user has joined.

#### Events
Each event object has the following fields:

- group_id: The unique identifier of the group that organised this event.
- name: The title of the event.
- description: The description of the event.
- created: Timestamp of the moment the event was created by the organiser.
- time: The timestamp of when the event will start (or has started).
- duration: The duration of the event, in seconds.
- rsvp_limit: The maximum number of YES RSVPs that this event will allow.
- venue_id: Unique identifier of the venue where this event takes place (see below).
- status: The status of the event. Possible values include 'past' and 'upcoming', meaning the the event has already taken place or that the event is planned for the future respectively. Keep in mind that this dataset was created at some point in the past, so an event marked as upcoming might not actually have a time in the past given the time of creating the solution.
- rsvps: An array of RSVP objects, which contain the following fields:
    - user_id: The unique identifier of the user that RSVPed for this event.
    - when: Timestamp of the moment the user gave their RSVP.
    - response: Yes or No, the indication of whether this user will attend the event.
    - guests: If permitted, the number of guests that the user is planning to bring to the event.

#### Venues
Each venue has the following fields:

- venue_id: A unique identifier for this venue.
- name: The name of the venue.
- city: The city where the venue is located.
- country: The country where the venue is located.
- lat: The lattitude of the venue location.
- lon: The longitude of the vanue location.

### Evaluation
The evaluation of your solution is based on a presentation given by you for members of our team and on the solution itself. Please provide us with the working solution beforehand (short notice is OK, doesn't have to be weeks before).

The goal of this assignment and the presentation is to assess candidates' skills in the following areas:

- Mathematics / statistics
- Machine learning
- Computer programming
- Communication (can you unambiguously explain your approach to future colleagues)
- Creativity / curiosity (while running some form of autocorrelation might yield reasonable results, we care about your intuition in approaching the problem)

The predictive model that you use is *not* benchmarked against any known state of the art or other pre-existing solutions (we have a lot of those). We care about the reasoning behind it, but understand that creating a superior model to a complex problem will take substantial time and many iterations. This is a guideline to ensure that you do not get stuck in optimization.

We care about your ability to create a data driven solution that is useful for end users. In the end we are about creating software for our clients that will help them improve their organization. The result should fit that description.

Typically such a solution would include a user interface, but it is left out of scope because of the time constraints that apply. For this reason we chose a REST web service as interface.

###Questions
In case of questions or uncertainty you can send e-mail to [rob.harkink@tnt-digital.com](mailto:rob.harkink@tnt-digital.com).
