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
        # Query parameters. The query parameters vary depending on the module type.
        # 
        # - QueryTopo
        # ```
        # {
        #     "regionId": string,  #Region ID
        #     "startTime": string, #Start time in the format of yyyy-MM-dd HH:mm:ss
        #     "endTime": string, #End time in the format of yyyy-MM-dd HH:mm:ss
        #     "edgeFilter": { #Edge filter conditions
        #         "includeTypes": [enum], #Edge types to include
        #         "excludeTypes": [enum], #Edge types to exclude
        #         "fromNodeFilter": { #Source node filter conditions
        #             "includeEntityTypes": [enum] #Entity types to include
        #             "excludeEntityTypes": [enum] #Entity types to exclude
        #         },
        #         "toNodeFilter": {  #Target node filter conditions
        #             "includeEntityTypes": [enum] #Entity types to include
        #             "excludeEntityTypes": [enum] #Entity types to exclude
        #         }
        #     },
        #     "includeIsolatedNodes": boolean, #Whether to include isolated nodes
        #     "isolatedNodeFilter": { # Isolated node filter conditions
        #         "includeEntityTypes": [enum] #Entity types to include
        #         "excludeEntityTypes": [enum] #Entity types to exclude
        #      },
        #     "queryMetrics": boolean, # Whether to synchronously query related RED metrics when querying topology
        #     "timeoutSecs": int, # Metrics query timeout in seconds
        # 	"redOption": { #Metrics query control options
        # 		"skipRt": boolean,  # Whether to skip querying RT metrics
        # 		"skipCount": boolean, # Whether to skip querying request count metrics
        # 		"skipError": boolean # Whether to skip querying error count metrics
        # 	}
        # }
        # 
        # ```
        # 
        # - QueryTopoRed
        # 
        # ```
        # {
        #     "regionId": string,  #Region ID
        #     "startTime": string, #Start time in the format of yyyy-MM-dd HH:mm:ss
        #     "endTime": string,   #End time in the format of yyyy-MM-dd HH:mm:ss
        #     "edgeIds": [string]  #Edge IDs to query
        #     "nodeIds": [string]  #Node IDs to query
        #     "redOption": { #Metrics query control options
        #         "skipRt": boolean,  # Whether to skip querying RT metrics
        #         "skipCount": boolean, # Whether to skip querying request count metrics
        #         "skipError": boolean # Whether to skip querying error count metrics
        #     }
        # }
        # 
        # ```
        # 
        # This parameter is required.
        self.data = data
        # Module type
        # - QueryTopo 
        #   
        #     Topology query feature. A topology consists of edges and nodes. Each edge has a corresponding type, each node has a corresponding entity, and each entity has its type. By setting the edge type, node type, query time range, and other filter parameters, you can filter out the required topology data.
        # 
        # - QueryTopoRed
        #     
        #     Topology RED metrics (request count, latency, error count) query. When querying a topology with the metrics query option enabled, the topology may be too large to retrieve all metrics data. This feature allows users to actively query metrics data for specified nodes and edges.
        # 
        # 
        # Note: The above features are in canary release and are not enabled by default. To enable them, please contact ARMS on-call support.
        # 
        # This parameter is required.
        self.module = module
        # Region ID.
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

