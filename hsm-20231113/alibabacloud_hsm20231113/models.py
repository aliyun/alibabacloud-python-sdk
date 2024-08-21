# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class ConfigClusterSubnetRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        region_id: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.v_switch_ids = v_switch_ids
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ConfigClusterSubnetShrinkRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        region_id: str = None,
        v_switch_ids_shrink: str = None,
        vpc_id: str = None,
    ):
        # This parameter is required.
        self.cluster_id = cluster_id
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.v_switch_ids_shrink = v_switch_ids_shrink
        # This parameter is required.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.v_switch_ids_shrink is not None:
            result['VSwitchIds'] = self.v_switch_ids_shrink
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('VSwitchIds') is not None:
            self.v_switch_ids_shrink = m.get('VSwitchIds')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ConfigClusterSubnetResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConfigClusterSubnetResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfigClusterSubnetResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ConfigClusterSubnetResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


