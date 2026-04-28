# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CloudQueryAgentRequest(DaraModel):
    def __init__(
        self,
        active: int = None,
        cnos: str = None,
        comment: str = None,
        end_time: str = None,
        enterprise_id: int = None,
        limit: int = None,
        name: str = None,
        order: int = None,
        owner_id: int = None,
        qno: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        return_queue: int = None,
        start: int = None,
        start_time: str = None,
        status: int = None,
        webrtc_url_type: int = None,
    ):
        # 是否启用；正整数，只能是0或者1，0是停用，1是启用
        self.active = active
        # 多个座席号以英文逗号分隔 最多支持500个座席
        self.cnos = cnos
        # 通过座席备注信息检索；取值说明：前缀模糊匹配
        self.comment = comment
        # 创建时间终止时间点；取值说明："2019-10-11 23:59:59"
        self.end_time = end_time
        # 呼叫中心 id
        # 
        # This parameter is required.
        self.enterprise_id = enterprise_id
        # 查询条数；正整数，大于0，最大不能超过1000，默认10
        self.limit = limit
        # 通过座席名称检索；取值说明：前后缀模糊匹配
        self.name = name
        # 排序方式,按照创建时间排序；0正序 1倒序
        self.order = order
        self.owner_id = owner_id
        # 队列号；当qno不为空时，查询指定队列的所有座席记录
        self.qno = qno
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # 是否返回绑定座席的队列信息；0:不返回 1:需要返回 默认值:1
        self.return_queue = return_queue
        # 从第几条开始；正整数，大于等于0，默认0
        self.start = start
        # 创建时间起始时间点；取值说明："2019-10-11 00:00:00"
        self.start_time = start_time
        # 是否在线；正整数，只能是0或者1，0是离线，1是在线
        self.status = status
        # webrtc软电话返回地址；取值说明：0：企业默认 1：公网域名 2：专线域名 3：公网IP 4：专线IP
        self.webrtc_url_type = webrtc_url_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active is not None:
            result['Active'] = self.active

        if self.cnos is not None:
            result['Cnos'] = self.cnos

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.enterprise_id is not None:
            result['EnterpriseId'] = self.enterprise_id

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.name is not None:
            result['Name'] = self.name

        if self.order is not None:
            result['Order'] = self.order

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.qno is not None:
            result['Qno'] = self.qno

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.return_queue is not None:
            result['ReturnQueue'] = self.return_queue

        if self.start is not None:
            result['Start'] = self.start

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.webrtc_url_type is not None:
            result['WebrtcUrlType'] = self.webrtc_url_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')

        if m.get('Cnos') is not None:
            self.cnos = m.get('Cnos')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EnterpriseId') is not None:
            self.enterprise_id = m.get('EnterpriseId')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Qno') is not None:
            self.qno = m.get('Qno')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ReturnQueue') is not None:
            self.return_queue = m.get('ReturnQueue')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('WebrtcUrlType') is not None:
            self.webrtc_url_type = m.get('WebrtcUrlType')

        return self

