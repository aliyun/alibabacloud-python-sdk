# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DescribeApplicationSlbsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeApplicationSlbsResponseBodyData = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # Indicates whether the information about the SLB instances that are associated with an application was obtained successfully. Valid values:
        # 
        # *   **true**: indicates that the information was obtained successfully.
        # *   **false**: indicates that the information failed to be obtained.
        self.code = code
        # The returned data.
        self.data = data
        # The HTTP status code. Valid values:
        # 
        # *   **2xx**: indicates that the request was successful.
        # *   **3xx**: indicates that the request was redirected.
        # *   **4xx**: indicates that the request was invalid.
        # *   **5xx**: indicates that a server error occurred.
        self.error_code = error_code
        # The ID of the trace. It can be used to query the details of a request.
        self.message = message
        # The returned message.
        # 
        # *   **success** is returned when the request succeeds.
        # *   An error code is returned when the request fails.
        self.request_id = request_id
        self.success = success
        # The returned data.
        self.trace_id = trace_id

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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeApplicationSlbsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class DescribeApplicationSlbsResponseBodyData(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        cluster_id: str = None,
        internet: List[main_models.DescribeApplicationSlbsResponseBodyDataInternet] = None,
        internet_ip: str = None,
        internet_slb_charge_type: str = None,
        internet_slb_expired: bool = None,
        internet_slb_id: str = None,
        intranet: List[main_models.DescribeApplicationSlbsResponseBodyDataIntranet] = None,
        intranet_ip: str = None,
        intranet_slb_charge_type: str = None,
        intranet_slb_expired: bool = None,
        intranet_slb_id: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.cluster_id = cluster_id
        # The configurations of the Internet-facing SLB instance.
        self.internet = internet
        # The ID of the Internet-facing SLB instance.
        self.internet_ip = internet_ip
        self.internet_slb_charge_type = internet_slb_charge_type
        self.internet_slb_expired = internet_slb_expired
        # Configurations of Internet-facing SLB instances.
        self.internet_slb_id = internet_slb_id
        # The configurations of the internal-facing SLB instance.
        self.intranet = intranet
        # The error code.
        # 
        # *   The **ErrorCode** parameter is not returned when the request succeeds.
        # *   The **ErrorCode** parameter is returned when the request fails. For more information, see **Error codes** in this topic.
        self.intranet_ip = intranet_ip
        self.intranet_slb_charge_type = intranet_slb_charge_type
        self.intranet_slb_expired = intranet_slb_expired
        # The IP address of the internal-facing SLB instance.
        self.intranet_slb_id = intranet_slb_id

    def validate(self):
        if self.internet:
            for v1 in self.internet:
                 if v1:
                    v1.validate()
        if self.intranet:
            for v1 in self.intranet:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        result['Internet'] = []
        if self.internet is not None:
            for k1 in self.internet:
                result['Internet'].append(k1.to_map() if k1 else None)

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.internet_slb_charge_type is not None:
            result['InternetSlbChargeType'] = self.internet_slb_charge_type

        if self.internet_slb_expired is not None:
            result['InternetSlbExpired'] = self.internet_slb_expired

        if self.internet_slb_id is not None:
            result['InternetSlbId'] = self.internet_slb_id

        result['Intranet'] = []
        if self.intranet is not None:
            for k1 in self.intranet:
                result['Intranet'].append(k1.to_map() if k1 else None)

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.intranet_slb_charge_type is not None:
            result['IntranetSlbChargeType'] = self.intranet_slb_charge_type

        if self.intranet_slb_expired is not None:
            result['IntranetSlbExpired'] = self.intranet_slb_expired

        if self.intranet_slb_id is not None:
            result['IntranetSlbId'] = self.intranet_slb_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        self.internet = []
        if m.get('Internet') is not None:
            for k1 in m.get('Internet'):
                temp_model = main_models.DescribeApplicationSlbsResponseBodyDataInternet()
                self.internet.append(temp_model.from_map(k1))

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('InternetSlbChargeType') is not None:
            self.internet_slb_charge_type = m.get('InternetSlbChargeType')

        if m.get('InternetSlbExpired') is not None:
            self.internet_slb_expired = m.get('InternetSlbExpired')

        if m.get('InternetSlbId') is not None:
            self.internet_slb_id = m.get('InternetSlbId')

        self.intranet = []
        if m.get('Intranet') is not None:
            for k1 in m.get('Intranet'):
                temp_model = main_models.DescribeApplicationSlbsResponseBodyDataIntranet()
                self.intranet.append(temp_model.from_map(k1))

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('IntranetSlbChargeType') is not None:
            self.intranet_slb_charge_type = m.get('IntranetSlbChargeType')

        if m.get('IntranetSlbExpired') is not None:
            self.intranet_slb_expired = m.get('IntranetSlbExpired')

        if m.get('IntranetSlbId') is not None:
            self.intranet_slb_id = m.get('IntranetSlbId')

        return self

class DescribeApplicationSlbsResponseBodyDataIntranet(DaraModel):
    def __init__(
        self,
        connection_drain_timeout: int = None,
        cookie: str = None,
        cookie_timeout: int = None,
        create_time: int = None,
        enable_connection_drain: bool = None,
        https_ca_cert_id: str = None,
        https_cert_id: str = None,
        port: int = None,
        protocol: str = None,
        sticky_session: bool = None,
        sticky_session_type: str = None,
        target_port: int = None,
        vserver_group_id: str = None,
    ):
        self.connection_drain_timeout = connection_drain_timeout
        self.cookie = cookie
        self.cookie_timeout = cookie_timeout
        # The timestamp when the canary release rule was created.
        self.create_time = create_time
        self.enable_connection_drain = enable_connection_drain
        self.https_ca_cert_id = https_ca_cert_id
        # The supported protocol.
        self.https_cert_id = https_cert_id
        # The IP address of the Internet-facing SLB instance.
        self.port = port
        # The container port.
        self.protocol = protocol
        self.sticky_session = sticky_session
        self.sticky_session_type = sticky_session_type
        # The port specified for the SLB listener.
        self.target_port = target_port
        self.vserver_group_id = vserver_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_drain_timeout is not None:
            result['ConnectionDrainTimeout'] = self.connection_drain_timeout

        if self.cookie is not None:
            result['Cookie'] = self.cookie

        if self.cookie_timeout is not None:
            result['CookieTimeout'] = self.cookie_timeout

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.enable_connection_drain is not None:
            result['EnableConnectionDrain'] = self.enable_connection_drain

        if self.https_ca_cert_id is not None:
            result['HttpsCaCertId'] = self.https_ca_cert_id

        if self.https_cert_id is not None:
            result['HttpsCertId'] = self.https_cert_id

        if self.port is not None:
            result['Port'] = self.port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.sticky_session is not None:
            result['StickySession'] = self.sticky_session

        if self.sticky_session_type is not None:
            result['StickySessionType'] = self.sticky_session_type

        if self.target_port is not None:
            result['TargetPort'] = self.target_port

        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionDrainTimeout') is not None:
            self.connection_drain_timeout = m.get('ConnectionDrainTimeout')

        if m.get('Cookie') is not None:
            self.cookie = m.get('Cookie')

        if m.get('CookieTimeout') is not None:
            self.cookie_timeout = m.get('CookieTimeout')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EnableConnectionDrain') is not None:
            self.enable_connection_drain = m.get('EnableConnectionDrain')

        if m.get('HttpsCaCertId') is not None:
            self.https_ca_cert_id = m.get('HttpsCaCertId')

        if m.get('HttpsCertId') is not None:
            self.https_cert_id = m.get('HttpsCertId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('StickySession') is not None:
            self.sticky_session = m.get('StickySession')

        if m.get('StickySessionType') is not None:
            self.sticky_session_type = m.get('StickySessionType')

        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')

        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')

        return self

class DescribeApplicationSlbsResponseBodyDataInternet(DaraModel):
    def __init__(
        self,
        connection_drain_timeout: int = None,
        cookie: str = None,
        cookie_timeout: int = None,
        create_time: int = None,
        enable_connection_drain: bool = None,
        https_ca_cert_id: str = None,
        https_cert_id: str = None,
        port: int = None,
        protocol: str = None,
        sticky_session: bool = None,
        sticky_session_type: str = None,
        target_port: int = None,
        vserver_group_id: str = None,
    ):
        self.connection_drain_timeout = connection_drain_timeout
        self.cookie = cookie
        self.cookie_timeout = cookie_timeout
        # The timestamp when the canary release rule was created.
        self.create_time = create_time
        self.enable_connection_drain = enable_connection_drain
        self.https_ca_cert_id = https_ca_cert_id
        # The supported protocol.
        self.https_cert_id = https_cert_id
        # The ID of the internal-facing SLB instance.
        self.port = port
        # The container port.
        self.protocol = protocol
        self.sticky_session = sticky_session
        self.sticky_session_type = sticky_session_type
        # The port specified for the SLB listener.
        self.target_port = target_port
        self.vserver_group_id = vserver_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_drain_timeout is not None:
            result['ConnectionDrainTimeout'] = self.connection_drain_timeout

        if self.cookie is not None:
            result['Cookie'] = self.cookie

        if self.cookie_timeout is not None:
            result['CookieTimeout'] = self.cookie_timeout

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.enable_connection_drain is not None:
            result['EnableConnectionDrain'] = self.enable_connection_drain

        if self.https_ca_cert_id is not None:
            result['HttpsCaCertId'] = self.https_ca_cert_id

        if self.https_cert_id is not None:
            result['HttpsCertId'] = self.https_cert_id

        if self.port is not None:
            result['Port'] = self.port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.sticky_session is not None:
            result['StickySession'] = self.sticky_session

        if self.sticky_session_type is not None:
            result['StickySessionType'] = self.sticky_session_type

        if self.target_port is not None:
            result['TargetPort'] = self.target_port

        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionDrainTimeout') is not None:
            self.connection_drain_timeout = m.get('ConnectionDrainTimeout')

        if m.get('Cookie') is not None:
            self.cookie = m.get('Cookie')

        if m.get('CookieTimeout') is not None:
            self.cookie_timeout = m.get('CookieTimeout')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EnableConnectionDrain') is not None:
            self.enable_connection_drain = m.get('EnableConnectionDrain')

        if m.get('HttpsCaCertId') is not None:
            self.https_ca_cert_id = m.get('HttpsCaCertId')

        if m.get('HttpsCertId') is not None:
            self.https_cert_id = m.get('HttpsCertId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('StickySession') is not None:
            self.sticky_session = m.get('StickySession')

        if m.get('StickySessionType') is not None:
            self.sticky_session_type = m.get('StickySessionType')

        if m.get('TargetPort') is not None:
            self.target_port = m.get('TargetPort')

        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')

        return self

