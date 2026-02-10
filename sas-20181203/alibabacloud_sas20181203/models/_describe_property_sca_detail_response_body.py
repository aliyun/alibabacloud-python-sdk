# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribePropertyScaDetailResponseBody(DaraModel):
    def __init__(
        self,
        page_info: main_models.DescribePropertyScaDetailResponseBodyPageInfo = None,
        propertys: List[main_models.DescribePropertyScaDetailResponseBodyPropertys] = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # The details about the asset fingerprints returned.
        self.propertys = propertys
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.propertys:
            for v1 in self.propertys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        result['Propertys'] = []
        if self.propertys is not None:
            for k1 in self.propertys:
                result['Propertys'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.DescribePropertyScaDetailResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        self.propertys = []
        if m.get('Propertys') is not None:
            for k1 in m.get('Propertys'):
                temp_model = main_models.DescribePropertyScaDetailResponseBodyPropertys()
                self.propertys.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePropertyScaDetailResponseBodyPropertys(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        biz_type_dispaly: str = None,
        cmdline: str = None,
        config_path: str = None,
        container_name: str = None,
        create_timestamp: int = None,
        image_name: str = None,
        instance_id: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        ip: str = None,
        listen_ip: str = None,
        listen_protocol: str = None,
        listen_status: str = None,
        name: str = None,
        path: str = None,
        pid: str = None,
        pod_name: str = None,
        port: str = None,
        ppid: str = None,
        process_started: int = None,
        process_user: str = None,
        proof: str = None,
        runtime_env_version: str = None,
        type: str = None,
        uuid: str = None,
        version: str = None,
        web_path: str = None,
    ):
        # The type of the middleware, database, or web service. Valid values:
        # 
        # *   **system_service**: system service
        # *   **software_library**: software library
        # *   **docker_component**: container component
        # *   **database**: database
        # *   **web_container**: web container
        # *   **jar**: JAR package
        # *   **web_framework**: web framework
        self.biz_type = biz_type
        # The display name of the type of the middleware, database, or web service . Valid values:
        # 
        # *   System service
        # *   Software library
        # *   Container component
        # *   Database
        # *   Web container
        # *   JAR package
        # *   Web framework
        self.biz_type_dispaly = biz_type_dispaly
        # The command line of the process.
        self.cmdline = cmdline
        # The path to the configuration file.
        self.config_path = config_path
        # The name of the container.
        self.container_name = container_name
        # The latest collection timestamp, which indicates the last timestamp when Security Center collected the information about the middleware, database, or web service. Unit: milliseconds.
        self.create_timestamp = create_timestamp
        # The name of the image.
        self.image_name = image_name
        # The ID of the server on which the middleware, database, or web service is run.
        self.instance_id = instance_id
        # The name of the server on which the middleware, database, or web service is run.
        self.instance_name = instance_name
        # The public IP address of the server on which the middleware, database, or web service is run.
        self.internet_ip = internet_ip
        # The private IP address of the server on which the middleware, database, or web service is run.
        self.intranet_ip = intranet_ip
        # The public IP address of the server on which the middleware, database, or web service is run.
        self.ip = ip
        # The IP address that the process monitors.
        self.listen_ip = listen_ip
        # The protocol of the traffic on which the process listens. Valid values:
        # 
        # *   **UDP**
        # *   **TCP**
        self.listen_protocol = listen_protocol
        # The listening status of the process. Valid values:
        # 
        # *   **NONE**: not listening
        # *   **LISTEN**: listening
        self.listen_status = listen_status
        # The name of the middleware, database, or web service.
        self.name = name
        # The path of the middleware, database, or web service.
        self.path = path
        # The PID.
        self.pid = pid
        # The name of the Kubernetes pod.
        self.pod_name = pod_name
        # The port of the middleware, database, or web service.
        self.port = port
        # The ID of the parent process.
        self.ppid = ppid
        # The timestamp when the process starts. Unit: milliseconds.
        self.process_started = process_started
        # The name of the user who runs the process.
        self.process_user = process_user
        # The version verification information about the middleware, database, or web service.
        self.proof = proof
        # The version of the runtime environment.
        # 
        # >  The value of this parameter can be the Java Development Kit (JDK) version of the runtime environment for a Java process.
        self.runtime_env_version = runtime_env_version
        # The type of the middleware, database, or web service.
        self.type = type
        # The UUID of the server on which the middleware, database, or web service is run.
        self.uuid = uuid
        # The version of the middleware, database, or web service.
        self.version = version
        # The web directory.
        self.web_path = web_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.biz_type_dispaly is not None:
            result['BizTypeDispaly'] = self.biz_type_dispaly

        if self.cmdline is not None:
            result['Cmdline'] = self.cmdline

        if self.config_path is not None:
            result['ConfigPath'] = self.config_path

        if self.container_name is not None:
            result['ContainerName'] = self.container_name

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.listen_ip is not None:
            result['ListenIp'] = self.listen_ip

        if self.listen_protocol is not None:
            result['ListenProtocol'] = self.listen_protocol

        if self.listen_status is not None:
            result['ListenStatus'] = self.listen_status

        if self.name is not None:
            result['Name'] = self.name

        if self.path is not None:
            result['Path'] = self.path

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.pod_name is not None:
            result['PodName'] = self.pod_name

        if self.port is not None:
            result['Port'] = self.port

        if self.ppid is not None:
            result['Ppid'] = self.ppid

        if self.process_started is not None:
            result['ProcessStarted'] = self.process_started

        if self.process_user is not None:
            result['ProcessUser'] = self.process_user

        if self.proof is not None:
            result['Proof'] = self.proof

        if self.runtime_env_version is not None:
            result['RuntimeEnvVersion'] = self.runtime_env_version

        if self.type is not None:
            result['Type'] = self.type

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        if self.version is not None:
            result['Version'] = self.version

        if self.web_path is not None:
            result['WebPath'] = self.web_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('BizTypeDispaly') is not None:
            self.biz_type_dispaly = m.get('BizTypeDispaly')

        if m.get('Cmdline') is not None:
            self.cmdline = m.get('Cmdline')

        if m.get('ConfigPath') is not None:
            self.config_path = m.get('ConfigPath')

        if m.get('ContainerName') is not None:
            self.container_name = m.get('ContainerName')

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('ListenIp') is not None:
            self.listen_ip = m.get('ListenIp')

        if m.get('ListenProtocol') is not None:
            self.listen_protocol = m.get('ListenProtocol')

        if m.get('ListenStatus') is not None:
            self.listen_status = m.get('ListenStatus')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('PodName') is not None:
            self.pod_name = m.get('PodName')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Ppid') is not None:
            self.ppid = m.get('Ppid')

        if m.get('ProcessStarted') is not None:
            self.process_started = m.get('ProcessStarted')

        if m.get('ProcessUser') is not None:
            self.process_user = m.get('ProcessUser')

        if m.get('Proof') is not None:
            self.proof = m.get('Proof')

        if m.get('RuntimeEnvVersion') is not None:
            self.runtime_env_version = m.get('RuntimeEnvVersion')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('WebPath') is not None:
            self.web_path = m.get('WebPath')

        return self

class DescribePropertyScaDetailResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        next_token: str = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The value of NextToken that is returned when the NextToken method is used.
        self.next_token = next_token
        # The number of entries returned per page. Default value: **10**.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

