# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeSubscriptionMetaResponseBody(DaraModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        http_status_code: str = None,
        request_id: str = None,
        subscription_meta_list: List[main_models.DescribeSubscriptionMetaResponseBodySubscriptionMetaList] = None,
        success: str = None,
    ):
        # The error code returned if the request failed.
        self.err_code = err_code
        # The error message returned if the request failed.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The ID of the request.
        self.request_id = request_id
        # The details of the subtasks.
        self.subscription_meta_list = subscription_meta_list
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.subscription_meta_list:
            for v1 in self.subscription_meta_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SubscriptionMetaList'] = []
        if self.subscription_meta_list is not None:
            for k1 in self.subscription_meta_list:
                result['SubscriptionMetaList'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.subscription_meta_list = []
        if m.get('SubscriptionMetaList') is not None:
            for k1 in m.get('SubscriptionMetaList'):
                temp_model = main_models.DescribeSubscriptionMetaResponseBodySubscriptionMetaList()
                self.subscription_meta_list.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeSubscriptionMetaResponseBodySubscriptionMetaList(DaraModel):
    def __init__(
        self,
        checkpoint: int = None,
        dblist: str = None,
        dproxy_url: str = None,
        sid: str = None,
        topic: str = None,
    ):
        # The consumer offset of the subtask. It is a UNIX timestamp that is generated when the client consumes the first data record. Unit: seconds.
        # 
        # >  You can use a search engine to obtain a UNIX timestamp converter.
        self.checkpoint = checkpoint
        # The objects of the subtask. For more information, see [Objects of DTS tasks](https://help.aliyun.com/document_detail/209545.html).
        self.dblist = dblist
        # The endpoint and port number of the change tracking instance.
        self.dproxy_url = dproxy_url
        # The consumer group ID of the subtask.
        self.sid = sid
        # The topic of the subtask.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checkpoint is not None:
            result['Checkpoint'] = self.checkpoint

        if self.dblist is not None:
            result['DBList'] = self.dblist

        if self.dproxy_url is not None:
            result['DProxyUrl'] = self.dproxy_url

        if self.sid is not None:
            result['Sid'] = self.sid

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Checkpoint') is not None:
            self.checkpoint = m.get('Checkpoint')

        if m.get('DBList') is not None:
            self.dblist = m.get('DBList')

        if m.get('DProxyUrl') is not None:
            self.dproxy_url = m.get('DProxyUrl')

        if m.get('Sid') is not None:
            self.sid = m.get('Sid')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

