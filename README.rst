Requirements for Fiber-permissions
==================================

The permissions will be enforced through the already present api. This means All actions exercised through the frontend. Actions through the backend will not have 
permission checking for now.

All page nodes displayed in the sidebar must only show the tree the user, or his group belongs to.

Listing Pages, ContentItems, PageContentItems, only returns 



Wat als 2 contenitems op 2 sites gebruikt worden?

Wat als de superadmin een object toevoegt/ edit? Welke rechten wordne aan het object gehangen?



Use cases
---------

Add a location
``````````````

A superuser adds a location via the backend. A location may be a page tree or a node with children. Along with the location, a group is created for this location.
