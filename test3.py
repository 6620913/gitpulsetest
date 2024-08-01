# Commit Summary

## Developer: Chris Corbo
**Category: Feature Development and Testing**
- Chris Corbo has been working on the dynamic renderer support, including its related locations and tests.
- Updated the location to pull renderer URL and improved test coverage.
- Worked on tasks associated with OpenRTB (Open Real-Time Bidding), such as moving to the ORTB converter [PB-1778].

## Developer: Demetrio Girardi
**Category: Asynchronous Testing and Refactoring**
- Stopped using the GreedyPromise and moved towards asynchronous testing across multiple modules like adxc, aso, blasto, criteo, improvedigital, etc.
- Worked on asynchronous tests involving userId, geolocation, and auctions.
- Implemented refactoring for GPP, TCF, and renamed timeout to delay.
- Reinstated GreedyPromise as a library and continued further asynchronous tests.
- Extracted the consent module config logic and fixed the greedy setTimeout issue.

## Commit Summary

### Developer: Chris Corbo
- Implemented dynamic renderer support and updated location to pull renderer URL.
- Performed multiple test updates and increased test coverage.
- Moved to ORTB converter labeled as [PB-1778].

### Developer: Demetrio Girardi
- Stopped using GreedyPromise and refactored GPP as well as TCF.
- Made several tests asynchronous, including adxc, aso, blasto, criteo, and auctions, among others.
- Reinstated GreedyPromise as a library and renamed it to PbPromise.
- Fixed issues in cmUtils timeout and Greedy setTimeout.
- Extracted consentManagement config parsing and consent module config logic.
- Resolved errors in 8podAnalytics tests.

Please check the detailed commit history for a comprehensive overview of changes in the codebase and modified files.
