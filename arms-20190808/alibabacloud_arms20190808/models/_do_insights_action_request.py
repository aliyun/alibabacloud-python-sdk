# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DoInsightsActionRequest(DaraModel):
    def __init__(
        self,
        data: str = None,
        module: str = None,
        region_id: str = None,
    ):
        # The query parameters. Different module types correspond to different query parameters.
        # 
        # *   QueryTopo
        # 
        # <!---->
        # 
        #     {
        #         "regionId": string,  # The region ID.
        #         "startTime": string, #. The start time. Format: yyyy-MM-dd HH:mm:ss.
        #         "endTime": string, # The end time. Format: yyyy-MM-dd HH:mm:ss.
        #         "edgeFilter": { # The edge filter condition.
        #             "includeTypes": [enum], # The edge types to be included.
        #             "excludeTypes": [enum], # The edge types to be excluded.
        #             "fromNodeFilter": { # The source node filter condition.
        #                 "includeEntityTypes": [enum] # The entity types to be included.
        #                 "excludeEntityTypes": [enum] #The entity types to be excluded.
        #             },
        #             "toNodeFilter": {  #The target node filter condition.
        #                 "includeEntityTypes": [enum] # The entity types to be included.
        #                 "excludeEntityTypes": [enum] #The entity types to be excluded.
        #             }
        #         },
        #         "includeIsolatedNodes": boolean, #Specifies whether to include isolated nodes.
        #         "isolatedNodeFilter": { # The isolated node filter condition.
        #             "includeEntityTypes": [enum] # The entity types to be included.
        #             "excludeEntityTypes": [enum] #The entity types to be excluded.
        #          },
        #         "queryMetrics": boolean, # Specifies whether to query RED metrics along with metrics.
        #         "timeoutSecs": int, # The timeout period of metric query.
        #     	"redOption": { # The metric query option.
        #     		"skipRt": boolean,  # Specifies whether to skip querying the response time.
        #     		"skipCount": boolean, # Specifies whether to skip querying the number of requests.
        #     		"skipError": boolean # Specifies whether to skip querying the number of errors.
        #     	}
        #     }
        # 
        # *   QueryTopoRed
        # 
        # <!---->
        # 
        #     {
        #         "regionId": string,  # The region ID.
        #         "startTime": string, #. The start time. Format: yyyy-MM-dd HH:mm:ss.
        #         "endTime": string,   # The end time. Format: yyyy-MM-dd HH:mm:ss.
        #         "edgeIds": [string]  # The edge ID to be queried.
        #         "nodeIds": [string]  # The node ID to be queried.
        #         "redOption": { # The metric query option.
        #             "skipRt": boolean,  # Specifies whether to skip querying the response time.
        #             "skipRt": boolean,  # Specifies whether to skip querying the number of requests.
        #             "skipError": boolean # Specifies whether to skip querying the number of errors.
        #         }
        #     }
        # 
        # This parameter is required.
        self.data = data
        # The module type.
        # 
        # *   QueryTopo
        # 
        #     Queries topologies. A topology consists of edges and nodes, where each edge has a corresponding type and each node corresponds to an entity, which also has its type. By setting filter parameters such as the type of edges, the type of nodes, and the query time range, you can filter out the required topology data.
        # 
        # *   QueryTopoRed
        # 
        #     Queries topology RED metrics (number of requests, duration, number of errors). When querying a topology with the metric query option enabled, it might not be possible to retrieve all metric data due to the topology being too large. This module allows users to actively query for metric data of specified nodes and edges.
        # 
        # Note: The aforementioned modules are currently in a canary release phase and are not enabled by default. If you need to enable them, please contact the ARMS on-duty number.
        # 
        # Valid values:
        # 
        # *   QueryTopoRed
        # *   QueryTopo
        # 
        # This parameter is required.
        self.module = module
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.module is not None:
            result['Module'] = self.module

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Module') is not None:
            self.module = m.get('Module')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

