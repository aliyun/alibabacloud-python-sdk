2026-03-20 Version: 2.0.3
- Update API CreateServerGroup: add request parameters HealthCheckConfig.HealthCheckExp.
- Update API CreateServerGroup: add request parameters HealthCheckConfig.HealthCheckReq.
- Update API ListServerGroups: add response parameters Body.ServerGroups.$.HealthCheckConfig.HealthCheckExp.
- Update API ListServerGroups: add response parameters Body.ServerGroups.$.HealthCheckConfig.HealthCheckReq.
- Update API UpdateServerGroupAttribute: add request parameters HealthCheckConfig.HealthCheckExp.
- Update API UpdateServerGroupAttribute: add request parameters HealthCheckConfig.HealthCheckReq.


2025-07-10 Version: 2.0.2
- Update API CreateListener: add request parameters TcpIdleTimeout.
- Update API GetListenerAttribute: add response parameters Body.TcpIdleTimeout.
- Update API ListListeners: add response parameters Body.Listeners.$.TcpIdleTimeout.
- Update API UpdateListenerAttribute: add request parameters TcpIdleTimeout.


2025-04-17 Version: 2.0.1
- Update API CreateServerGroup: add request parameters ServerFailoverMode.
- Update API GetLoadBalancerAttribute: add response parameters Body.TrafficMode.
- Update API ListLoadBalancers: add request parameters TrafficMode.
- Update API ListServerGroups: add response parameters Body.ServerGroups.$.ServerFailoverMode.
- Update API UpdateLoadBalancerAttribute: add request parameters TrafficMode.
- Update API UpdateServerGroupAttribute: add request parameters ServerFailoverMode.


2024-10-18 Version: 2.0.0
- Update API ListListeners: update param Skip.


2024-10-16 Version: 1.0.0
- Generated python 2024-04-15 for Gwlb.

