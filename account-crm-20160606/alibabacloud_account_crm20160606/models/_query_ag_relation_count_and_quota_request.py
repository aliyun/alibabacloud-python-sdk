# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryAgRelationCountAndQuotaRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        caller_bid: int = None,
        caller_parent_id: int = None,
        caller_type: str = None,
        caller_uid: int = None,
        mpk: str = None,
        null_object: bool = None,
        request_id: str = None,
        security_token: str = None,
        source_ip: str = None,
        sts_token_caller_bid: int = None,
        sts_token_caller_uid: int = None,
        sts_token_role_id: int = None,
        version: str = None,
    ):
        self.app_name = app_name
        self.caller_bid = caller_bid
        self.caller_parent_id = caller_parent_id
        self.caller_type = caller_type
        self.caller_uid = caller_uid
        self.mpk = mpk
        self.null_object = null_object
        self.request_id = request_id
        self.security_token = security_token
        self.source_ip = source_ip
        self.sts_token_caller_bid = sts_token_caller_bid
        self.sts_token_caller_uid = sts_token_caller_uid
        self.sts_token_role_id = sts_token_role_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.caller_bid is not None:
            result['CallerBid'] = self.caller_bid

        if self.caller_parent_id is not None:
            result['CallerParentId'] = self.caller_parent_id

        if self.caller_type is not None:
            result['CallerType'] = self.caller_type

        if self.caller_uid is not None:
            result['CallerUid'] = self.caller_uid

        if self.mpk is not None:
            result['Mpk'] = self.mpk

        if self.null_object is not None:
            result['NullObject'] = self.null_object

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.security_token is not None:
            result['SecurityToken'] = self.security_token

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.sts_token_caller_bid is not None:
            result['StsTokenCallerBid'] = self.sts_token_caller_bid

        if self.sts_token_caller_uid is not None:
            result['StsTokenCallerUid'] = self.sts_token_caller_uid

        if self.sts_token_role_id is not None:
            result['StsTokenRoleId'] = self.sts_token_role_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('CallerBid') is not None:
            self.caller_bid = m.get('CallerBid')

        if m.get('CallerParentId') is not None:
            self.caller_parent_id = m.get('CallerParentId')

        if m.get('CallerType') is not None:
            self.caller_type = m.get('CallerType')

        if m.get('CallerUid') is not None:
            self.caller_uid = m.get('CallerUid')

        if m.get('Mpk') is not None:
            self.mpk = m.get('Mpk')

        if m.get('NullObject') is not None:
            self.null_object = m.get('NullObject')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('StsTokenCallerBid') is not None:
            self.sts_token_caller_bid = m.get('StsTokenCallerBid')

        if m.get('StsTokenCallerUid') is not None:
            self.sts_token_caller_uid = m.get('StsTokenCallerUid')

        if m.get('StsTokenRoleId') is not None:
            self.sts_token_role_id = m.get('StsTokenRoleId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

