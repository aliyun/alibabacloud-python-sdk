# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PutDataEventSelectorResponseBody(DaraModel):
    def __init__(
        self,
        data_event_selectors: str = None,
        request_id: str = None,
        trail_arn: str = None,
    ):
        # The configuration of the data event selector. This parameter is a JSON array that can contain a maximum of 20 elements.
        # 
        # Each element in the JSON array includes the following fields:
        # 
        # - `ServiceName`: The name of the Alibaba Cloud service that supports data events.
        # 
        # - `ReadWriteType`: The type of data event. Valid values: Read, Write, and All.
        # 
        # - `EventName`: This field contains the `Equals` and `NotEquals` subfields.
        # 
        #   For example, the following configuration specifies that only `GetObject`, `CopyObject`, and `AppendObject` events are delivered:
        # 
        #   `{"EventName":{"Equals":["GetObject","CopyObject","AppendObject"]}}`
        # 
        #   If you specify `NotEquals`, events other than `GetObject`, `CopyObject`, and `AppendObject` are delivered.
        # 
        # - `ResourceArn`: This field also contains the `Equals` and `NotEquals` subfields, similar to `EventName`. For example:
        # 
        #   `{"ResourceArn":{"Equals":[arn1,...,arnx]}}`
        self.data_event_selectors = data_event_selectors
        # The request ID.
        self.request_id = request_id
        # The Alibaba Cloud Resource Name (ARN) of the trail.
        self.trail_arn = trail_arn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_event_selectors is not None:
            result['DataEventSelectors'] = self.data_event_selectors

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.trail_arn is not None:
            result['TrailArn'] = self.trail_arn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataEventSelectors') is not None:
            self.data_event_selectors = m.get('DataEventSelectors')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TrailArn') is not None:
            self.trail_arn = m.get('TrailArn')

        return self

