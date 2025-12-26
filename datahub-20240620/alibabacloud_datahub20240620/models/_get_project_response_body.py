# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetProjectResponseBody(DaraModel):
    def __init__(
        self,
        comment: str = None,
        create_time: str = None,
        creator: str = None,
        project_name: str = None,
        request_id: str = None,
        storage: int = None,
        success: bool = None,
        update_time: str = None,
        vpc_whitelist: str = None,
    ):
        self.comment = comment
        self.create_time = create_time
        self.creator = creator
        self.project_name = project_name
        self.request_id = request_id
        self.storage = storage
        self.success = success
        self.update_time = update_time
        self.vpc_whitelist = vpc_whitelist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.storage is not None:
            result['Storage'] = self.storage

        if self.success is not None:
            result['Success'] = self.success

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.vpc_whitelist is not None:
            result['VpcWhitelist'] = self.vpc_whitelist

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Storage') is not None:
            self.storage = m.get('Storage')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VpcWhitelist') is not None:
            self.vpc_whitelist = m.get('VpcWhitelist')

        return self

