# Resources

This document describes the different resources that form this RESTful service, and their URL schema.

There are three main resources at this point:

- A user resource. It is stored in the database along with a password, when a user is created.
    - Base schema: `users/{username}`
    - A GET on this resource returns basic user "links"
    - A PUT on this resource creates a new user. A password needs to be delivered as part of the body.
    - A DELETE on this resource removes the user and all their messages from the system.
- The list of sent and received messages for a given user.
    - Base schema: `users/{user}/messages`
    - A GET on the list fetches all messages, both sent and received. More precisely, it returns links to GET requests for the messages. It also provides instructions for the submission of a new message. It would optionally allow for some query parameters (count, since date, only read/unread, only read or only sent).
    - A POST on the list creates a new message. You must specify a recipient, a subject line and a text body.
    - No PUT/DELETE allowed.
- An individual message, identified via an increasing id.
    - Base schema: `messages/{msg_id}`
    - A GET on the message provides all the information for the message. It also offers a link to reply to the message, as well as links to the various tags for the message.
    - A POST on the message can be used to mark the message as read.
    - A DELETE will delete the message.
    - No PUT allowed.
- A message with a tag attached to it.
    - Base schema: `messages/{msg_id}/tag/{tag}`
    - A GET on such a schema returns 200 or 404 based on whether the tag is associated with the message.
    - A PUT on such a schema associates a specific tag with the specific message.
    - A DELETE on such a schema will remove that tag from the message.
    - No POST allowed.

At this point we are not concerned with permissions questions, but later on we will be.

Here is a tabular representation of the same information:

| Schema                     | GET   | PUT    | POST      | DELETE          |
| :-----------------------   | :---- | :--    | :-------- | :-------------- |
| `users/{user}`             | info  | create | N/A       | delete, cascade |
| `users/{user}/messages`    | list  | N/A    | new msg   | N/A             |
| `messages/{id}`            | view  | N/A    | mark read | delete          |
| `messages/{id}/tags/{tag}` | check | tag    | N/A       | untag           |

## Request specifics

We will now discuss each of these resources and request types in detail, outlining the input and output expected as well as the kinds of possible errors.

### `GET users/{user}`

### `PUT users/{user}`

### `DELETE users/{user}`

### `GET users/{user}/messages`

### `POST users/{user}/messages`

### `GET messages/{id}`

### `POST messages/{id}`

### `DELETE messages/{id}`

### `GET messages/{id}/tags/{tag}`

### `PUT messages/{id}/tags/{tag}`

### `DELETE messages/{id}/tags/{tag}`
