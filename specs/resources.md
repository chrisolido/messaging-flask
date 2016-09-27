# Resources

This document describes the different resources that form this RESTful service, and their URL schema.

There are two main resources at this point:

- The list of sent and received messages for a given user.
    - Base schema: `user/{user}/message`
    - A GET on the list fetches all messages, both sent and received. More precisely, it returns links to GET requests for the messages. It also provides instructions for the submission of a new message. It would optionally allow for some query parameters (count, since date, only read/unread, only read or only sent).
    - A POST on the list creates a new message. You must specify a recipient, a subject line and a text body.
    - No PUT/DELETE allowed.
- An individual message, identified via an md5 hash.
    - Base schema: `message/{msghash}`
    - A GET on the message provides all the information for the message.
    - A POST on the message can be used to mark the message as read.
    - A DELETE will delete the message.
    - No PUT allowed.

At this point we are not concerned with permissions questions, but later on we will be.

Here is a tabular representation of the same information:

| Schema                | GET  | PUT | POST      | DELETE   |
| :------------------   | :--- | :-- | :-------- | :------- |
| `user/{user}/message` | list | N/A | new msg   | N/A      |
| `message/{msghash}`   | view | N/A | mark read | delete   |

