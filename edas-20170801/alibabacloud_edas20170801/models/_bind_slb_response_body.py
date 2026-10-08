# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_edas20170801 import models as main_models
from darabonba.model import DaraModel

class BindSlbResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.BindSlbResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        self.code = code
        # The returned data.
        self.data = data
        # Additional information.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.BindSlbResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class BindSlbResponseBodyData(DaraModel):
    def __init__(
        self,
        ext_slb_id: str = None,
        ext_slb_ip: str = None,
        ext_slb_name: str = None,
        ext_vserver_group_id: str = None,
        slb_id: str = None,
        slb_ip: str = None,
        slb_name: str = None,
        slb_port: int = None,
        vserver_group_id: str = None,
    ):
        # The ID of the Internet-facing SLB instance.
        self.ext_slb_id = ext_slb_id
        # The IP address of the Internet-facing SLB instance.
        self.ext_slb_ip = ext_slb_ip
        # The name of the Internet-facing SLB instance.
        self.ext_slb_name = ext_slb_name
        # The ID of the vServer group for the Internet-facing SLB instance.
        self.ext_vserver_group_id = ext_vserver_group_id
        # The ID of the internal SLB instance.
        self.slb_id = slb_id
        # The IP address of the internal SLB instance.
        self.slb_ip = slb_ip
        # The name of the internal SLB instance.
        self.slb_name = slb_name
        # The listener port of the SLB instance.
        self.slb_port = slb_port
        # The ID of the internal vServer group.
        self.vserver_group_id = vserver_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ext_slb_id is not None:
            result['ExtSlbId'] = self.ext_slb_id

        if self.ext_slb_ip is not None:
            result['ExtSlbIp'] = self.ext_slb_ip

        if self.ext_slb_name is not None:
            result['ExtSlbName'] = self.ext_slb_name

        if self.ext_vserver_group_id is not None:
            result['ExtVServerGroupId'] = self.ext_vserver_group_id

        if self.slb_id is not None:
            result['SlbId'] = self.slb_id

        if self.slb_ip is not None:
            result['SlbIp'] = self.slb_ip

        if self.slb_name is not None:
            result['SlbName'] = self.slb_name

        if self.slb_port is not None:
            result['SlbPort'] = self.slb_port

        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtSlbId') is not None:
            self.ext_slb_id = m.get('ExtSlbId')

        if m.get('ExtSlbIp') is not None:
            self.ext_slb_ip = m.get('ExtSlbIp')

        if m.get('ExtSlbName') is not None:
            self.ext_slb_name = m.get('ExtSlbName')

        if m.get('ExtVServerGroupId') is not None:
            self.ext_vserver_group_id = m.get('ExtVServerGroupId')

        if m.get('SlbId') is not None:
            self.slb_id = m.get('SlbId')

        if m.get('SlbIp') is not None:
            self.slb_ip = m.get('SlbIp')

        if m.get('SlbName') is not None:
            self.slb_name = m.get('SlbName')

        if m.get('SlbPort') is not None:
            self.slb_port = m.get('SlbPort')

        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')

        return self

