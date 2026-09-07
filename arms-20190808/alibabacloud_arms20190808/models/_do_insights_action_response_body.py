# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DoInsightsActionResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # Status code. 200 indicates success; other status codes indicate exceptions.
        self.code = code
        # The return parameter type is related to the module value passed in.
        # 
        # - QueryTopo
        #    ```
        #   {
        # 	"nodes": [Object] #Node collection. See the Node definition in the supplementary description of return parameters.
        # 	"edges": [Object] #Edge collection. See the Edge definition in the supplementary description of return parameters.
        #   }
        #   ```
        # - QueryTopoRed
        # 
        #   ```
        #   {
        # 	"nodeRed": {
        # 		"nodeId": {
        # 			"count": double, #Total number of requests during the query period
        # 			"error": double, #Total number of errors during the query period
        # 			"rt": double, #Average latency during the query period, in milliseconds
        # 		}
        # 	},
        # 	"edgeRed": {
        # 		"edgeId": {
        # 		    "count": double, #Total number of requests during the query period
        # 			"error": double, #Total number of errors during the query period
        # 			"rt": double, #Average latency during the query period, in milliseconds
        # 		}
        # 	}
        # }
        #   ```
        self.data = data
        # The message returned when the call fails.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Whether the query is successful:
        # 
        # - `true`: Successful.
        # - `false`: Failed.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

