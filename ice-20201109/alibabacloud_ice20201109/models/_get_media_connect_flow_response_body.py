# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class GetMediaConnectFlowResponseBody(DaraModel):
    def __init__(
        self,
        content: main_models.GetMediaConnectFlowResponseBodyContent = None,
        description: str = None,
        request_id: str = None,
        retcode: int = None,
    ):
        # The response body.
        self.content = content
        # The call description.
        self.description = description
        # The ID of the request.
        self.request_id = request_id
        # The returned code. A value of 0 indicates the call is successful.
        self.retcode = retcode

    def validate(self):
        if self.content:
            self.content.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.retcode is not None:
            result['Retcode'] = self.retcode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            temp_model = main_models.GetMediaConnectFlowResponseBodyContent()
            self.content = temp_model.from_map(m.get('Content'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Retcode') is not None:
            self.retcode = m.get('Retcode')

        return self

class GetMediaConnectFlowResponseBodyContent(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        flow_failover: str = None,
        flow_id: str = None,
        flow_name: str = None,
        flow_region: str = None,
        flow_status: str = None,
        start_time: str = None,
    ):
        # The time when the flow was created.
        self.create_time = create_time
        self.flow_failover = flow_failover
        # The flow ID.
        self.flow_id = flow_id
        # The flow name.
        self.flow_name = flow_name
        self.flow_region = flow_region
        # The state of the flow.
        self.flow_status = flow_status
        # The time when the flow is started.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.flow_failover is not None:
            result['FlowFailover'] = self.flow_failover

        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.flow_name is not None:
            result['FlowName'] = self.flow_name

        if self.flow_region is not None:
            result['FlowRegion'] = self.flow_region

        if self.flow_status is not None:
            result['FlowStatus'] = self.flow_status

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('FlowFailover') is not None:
            self.flow_failover = m.get('FlowFailover')

        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')

        if m.get('FlowRegion') is not None:
            self.flow_region = m.get('FlowRegion')

        if m.get('FlowStatus') is not None:
            self.flow_status = m.get('FlowStatus')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

