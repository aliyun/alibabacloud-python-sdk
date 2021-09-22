# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class RunFunctionRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        body: str = None,
    ):
        self.space_id = space_id
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.body is not None:
            result['Body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        return self


class RunFunctionResponseBodyRuntimeMeta(TeaModel):
    def __init__(
        self,
        invocation_duration: int = None,
        request_id: str = None,
        billing_duration: int = None,
        max_memory_usage: int = None,
    ):
        self.invocation_duration = invocation_duration
        self.request_id = request_id
        self.billing_duration = billing_duration
        self.max_memory_usage = max_memory_usage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invocation_duration is not None:
            result['InvocationDuration'] = self.invocation_duration
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.billing_duration is not None:
            result['BillingDuration'] = self.billing_duration
        if self.max_memory_usage is not None:
            result['MaxMemoryUsage'] = self.max_memory_usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InvocationDuration') is not None:
            self.invocation_duration = m.get('InvocationDuration')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BillingDuration') is not None:
            self.billing_duration = m.get('BillingDuration')
        if m.get('MaxMemoryUsage') is not None:
            self.max_memory_usage = m.get('MaxMemoryUsage')
        return self


class RunFunctionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
        runtime_meta: RunFunctionResponseBodyRuntimeMeta = None,
    ):
        self.request_id = request_id
        self.result = result
        self.runtime_meta = runtime_meta

    def validate(self):
        if self.runtime_meta:
            self.runtime_meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.runtime_meta is not None:
            result['RuntimeMeta'] = self.runtime_meta.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('RuntimeMeta') is not None:
            temp_model = RunFunctionResponseBodyRuntimeMeta()
            self.runtime_meta = temp_model.from_map(m['RuntimeMeta'])
        return self


class RunFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RunFunctionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RunFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        filter_by: str = None,
        space_id: str = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.filter_by = filter_by
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.filter_by is not None:
            result['FilterBy'] = self.filter_by
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('FilterBy') is not None:
            self.filter_by = m.get('FilterBy')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class ListFunctionResponseBodyPaginator(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
        page_count: int = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.total = total
        self.page_count = page_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        return self


class ListFunctionResponseBodyDataListSpec(TeaModel):
    def __init__(
        self,
        timeout: str = None,
        runtime: str = None,
        instance_concurrency: int = None,
        memory: str = None,
    ):
        self.timeout = timeout
        self.runtime = runtime
        self.instance_concurrency = instance_concurrency
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.runtime is not None:
            result['Runtime'] = self.runtime
        if self.instance_concurrency is not None:
            result['InstanceConcurrency'] = self.instance_concurrency
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('Runtime') is not None:
            self.runtime = m.get('Runtime')
        if m.get('InstanceConcurrency') is not None:
            self.instance_concurrency = m.get('InstanceConcurrency')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class ListFunctionResponseBodyDataList(TeaModel):
    def __init__(
        self,
        timing_trigger_config: str = None,
        http_trigger_path: str = None,
        created_at: str = None,
        modified_at: str = None,
        name: str = None,
        desc: str = None,
        spec: ListFunctionResponseBodyDataListSpec = None,
    ):
        self.timing_trigger_config = timing_trigger_config
        self.http_trigger_path = http_trigger_path
        self.created_at = created_at
        self.modified_at = modified_at
        self.name = name
        self.desc = desc
        self.spec = spec

    def validate(self):
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timing_trigger_config is not None:
            result['TimingTriggerConfig'] = self.timing_trigger_config
        if self.http_trigger_path is not None:
            result['HttpTriggerPath'] = self.http_trigger_path
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.modified_at is not None:
            result['ModifiedAt'] = self.modified_at
        if self.name is not None:
            result['Name'] = self.name
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimingTriggerConfig') is not None:
            self.timing_trigger_config = m.get('TimingTriggerConfig')
        if m.get('HttpTriggerPath') is not None:
            self.http_trigger_path = m.get('HttpTriggerPath')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('ModifiedAt') is not None:
            self.modified_at = m.get('ModifiedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Spec') is not None:
            temp_model = ListFunctionResponseBodyDataListSpec()
            self.spec = temp_model.from_map(m['Spec'])
        return self


class ListFunctionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        paginator: ListFunctionResponseBodyPaginator = None,
        data_list: List[ListFunctionResponseBodyDataList] = None,
    ):
        self.request_id = request_id
        self.paginator = paginator
        self.data_list = data_list

    def validate(self):
        if self.paginator:
            self.paginator.validate()
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.paginator is not None:
            result['Paginator'] = self.paginator.to_map()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Paginator') is not None:
            temp_model = ListFunctionResponseBodyPaginator()
            self.paginator = temp_model.from_map(m['Paginator'])
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = ListFunctionResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        return self


class ListFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFunctionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWebHostingCertificateDetailRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        custom_domain: str = None,
    ):
        self.space_id = space_id
        self.custom_domain = custom_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.custom_domain is not None:
            result['CustomDomain'] = self.custom_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('CustomDomain') is not None:
            self.custom_domain = m.get('CustomDomain')
        return self


class GetWebHostingCertificateDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        cert_life: str = None,
        cert_type: str = None,
        cert_domain_name: str = None,
        server_certificate_status: str = None,
        cert_name: str = None,
        cert_expired_time: int = None,
    ):
        self.cert_life = cert_life
        self.cert_type = cert_type
        self.cert_domain_name = cert_domain_name
        self.server_certificate_status = server_certificate_status
        self.cert_name = cert_name
        self.cert_expired_time = cert_expired_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_life is not None:
            result['CertLife'] = self.cert_life
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.cert_domain_name is not None:
            result['CertDomainName'] = self.cert_domain_name
        if self.server_certificate_status is not None:
            result['ServerCertificateStatus'] = self.server_certificate_status
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.cert_expired_time is not None:
            result['CertExpiredTime'] = self.cert_expired_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertLife') is not None:
            self.cert_life = m.get('CertLife')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertDomainName') is not None:
            self.cert_domain_name = m.get('CertDomainName')
        if m.get('ServerCertificateStatus') is not None:
            self.server_certificate_status = m.get('ServerCertificateStatus')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('CertExpiredTime') is not None:
            self.cert_expired_time = m.get('CertExpiredTime')
        return self


class GetWebHostingCertificateDetailResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetWebHostingCertificateDetailResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetWebHostingCertificateDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetWebHostingCertificateDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetWebHostingCertificateDetailResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetWebHostingCertificateDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSpaceRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        desc: str = None,
        status: str = None,
    ):
        self.space_id = space_id
        self.desc = desc
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class UpdateSpaceResponseBody(TeaModel):
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


class UpdateSpaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateSpaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateSpaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveWebHostingCustomDomainConfigRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        force_redirect_type: str = None,
        domain_name: str = None,
    ):
        self.space_id = space_id
        self.force_redirect_type = force_redirect_type
        self.domain_name = domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.force_redirect_type is not None:
            result['ForceRedirectType'] = self.force_redirect_type
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('ForceRedirectType') is not None:
            self.force_redirect_type = m.get('ForceRedirectType')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        return self


class SaveWebHostingCustomDomainConfigResponseBody(TeaModel):
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


class SaveWebHostingCustomDomainConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SaveWebHostingCustomDomainConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SaveWebHostingCustomDomainConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionSpecResponseBodyMemoryList(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListFunctionSpecResponseBodyRuntimeList(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class ListFunctionSpecResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        memory_list: List[ListFunctionSpecResponseBodyMemoryList] = None,
        runtime_list: List[ListFunctionSpecResponseBodyRuntimeList] = None,
    ):
        self.request_id = request_id
        self.memory_list = memory_list
        self.runtime_list = runtime_list

    def validate(self):
        if self.memory_list:
            for k in self.memory_list:
                if k:
                    k.validate()
        if self.runtime_list:
            for k in self.runtime_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['MemoryList'] = []
        if self.memory_list is not None:
            for k in self.memory_list:
                result['MemoryList'].append(k.to_map() if k else None)
        result['RuntimeList'] = []
        if self.runtime_list is not None:
            for k in self.runtime_list:
                result['RuntimeList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.memory_list = []
        if m.get('MemoryList') is not None:
            for k in m.get('MemoryList'):
                temp_model = ListFunctionSpecResponseBodyMemoryList()
                self.memory_list.append(temp_model.from_map(k))
        self.runtime_list = []
        if m.get('RuntimeList') is not None:
            for k in m.get('RuntimeList'):
                temp_model = ListFunctionSpecResponseBodyRuntimeList()
                self.runtime_list.append(temp_model.from_map(k))
        return self


class ListFunctionSpecResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFunctionSpecResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFunctionSpecResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWechatOpenPlatformConfigRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        app_id: str = None,
    ):
        self.space_id = space_id
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DeleteWechatOpenPlatformConfigResponseBody(TeaModel):
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


class DeleteWechatOpenPlatformConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteWechatOpenPlatformConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteWechatOpenPlatformConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSpaceRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        desc: str = None,
        workspace_id: int = None,
    ):
        self.name = name
        self.desc = desc
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class CreateSpaceResponseBody(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        request_id: str = None,
    ):
        self.space_id = space_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSpaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSpaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSpaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenProductRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
    ):
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class OpenProductResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: str = None,
        synchro: str = None,
    ):
        self.request_id = request_id
        self.data = data
        self.synchro = synchro

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['data'] = self.data
        if self.synchro is not None:
            result['synchro'] = self.synchro
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('synchro') is not None:
            self.synchro = m.get('synchro')
        return self


class OpenProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OpenProductResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OpenProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenServiceRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        service_name: str = None,
    ):
        self.space_id = space_id
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class OpenServiceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_status: str = None,
        count: int = None,
    ):
        self.request_id = request_id
        self.service_status = service_status
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class OpenServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OpenServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OpenServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSpaceRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
    ):
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DeleteSpaceResponseBody(TeaModel):
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


class DeleteSpaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSpaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSpaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAntOpenPlatformConfigRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        app_id: str = None,
    ):
        self.space_id = space_id
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DeleteAntOpenPlatformConfigResponseBody(TeaModel):
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


class DeleteAntOpenPlatformConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAntOpenPlatformConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteAntOpenPlatformConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFCOpenStatusResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        request_id: str = None,
        is_authorized: bool = None,
    ):
        self.status = status
        self.request_id = request_id
        self.is_authorized = is_authorized

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.is_authorized is not None:
            result['IsAuthorized'] = self.is_authorized
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IsAuthorized') is not None:
            self.is_authorized = m.get('IsAuthorized')
        return self


class DescribeFCOpenStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFCOpenStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFCOpenStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFileUploadSignedUrlRequest(TeaModel):
    def __init__(
        self,
        filename: str = None,
        size: int = None,
        space_id: str = None,
        content_type: str = None,
    ):
        self.filename = filename
        self.size = size
        self.space_id = space_id
        self.content_type = content_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filename is not None:
            result['Filename'] = self.filename
        if self.size is not None:
            result['Size'] = self.size
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filename') is not None:
            self.filename = m.get('Filename')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        return self


class DescribeFileUploadSignedUrlResponseBody(TeaModel):
    def __init__(
        self,
        sign_url: str = None,
        request_id: str = None,
        id: str = None,
    ):
        self.sign_url = sign_url
        self.request_id = request_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sign_url is not None:
            result['SignUrl'] = self.sign_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SignUrl') is not None:
            self.sign_url = m.get('SignUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeFileUploadSignedUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFileUploadSignedUrlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFileUploadSignedUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFileRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        space_id: str = None,
    ):
        self.id = id
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DeleteFileResponseBody(TeaModel):
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


class DeleteFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteFileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDBImportTaskStatusRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        task_id: str = None,
    ):
        self.space_id = space_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class QueryDBImportTaskStatusResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        failed_count: str = None,
        request_id: str = None,
        detail_message: str = None,
        success_count: str = None,
    ):
        self.status = status
        self.failed_count = failed_count
        self.request_id = request_id
        self.detail_message = detail_message
        self.success_count = success_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.detail_message is not None:
            result['DetailMessage'] = self.detail_message
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DetailMessage') is not None:
            self.detail_message = m.get('DetailMessage')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        return self


class QueryDBImportTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDBImportTaskStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryDBImportTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterFileRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        space_id: str = None,
    ):
        self.id = id
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class RegisterFileResponseBody(TeaModel):
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


class RegisterFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RegisterFileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RegisterFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveAntOpenPlatformConfigRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        app_id: str = None,
        public_key: str = None,
        private_key: str = None,
        sign_mode: str = None,
        app_cert: str = None,
        public_cert: str = None,
        root_cert: str = None,
    ):
        self.space_id = space_id
        self.app_id = app_id
        self.public_key = public_key
        self.private_key = private_key
        self.sign_mode = sign_mode
        self.app_cert = app_cert
        self.public_cert = public_cert
        self.root_cert = root_cert

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.public_key is not None:
            result['PublicKey'] = self.public_key
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.sign_mode is not None:
            result['SignMode'] = self.sign_mode
        if self.app_cert is not None:
            result['AppCert'] = self.app_cert
        if self.public_cert is not None:
            result['PublicCert'] = self.public_cert
        if self.root_cert is not None:
            result['RootCert'] = self.root_cert
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('SignMode') is not None:
            self.sign_mode = m.get('SignMode')
        if m.get('AppCert') is not None:
            self.app_cert = m.get('AppCert')
        if m.get('PublicCert') is not None:
            self.public_cert = m.get('PublicCert')
        if m.get('RootCert') is not None:
            self.root_cert = m.get('RootCert')
        return self


class SaveAntOpenPlatformConfigResponseBody(TeaModel):
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


class SaveAntOpenPlatformConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SaveAntOpenPlatformConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SaveAntOpenPlatformConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFunctionRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        space_id: str = None,
    ):
        self.name = name
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DescribeFunctionResponseBodyFunctionSpec(TeaModel):
    def __init__(
        self,
        timeout: str = None,
        runtime: str = None,
        instance_concurrency: int = None,
        memory: str = None,
    ):
        self.timeout = timeout
        self.runtime = runtime
        self.instance_concurrency = instance_concurrency
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.runtime is not None:
            result['Runtime'] = self.runtime
        if self.instance_concurrency is not None:
            result['InstanceConcurrency'] = self.instance_concurrency
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('Runtime') is not None:
            self.runtime = m.get('Runtime')
        if m.get('InstanceConcurrency') is not None:
            self.instance_concurrency = m.get('InstanceConcurrency')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class DescribeFunctionResponseBodyFunction(TeaModel):
    def __init__(
        self,
        timing_trigger_config: str = None,
        http_trigger_path: str = None,
        created_at: str = None,
        name: str = None,
        modified_at: str = None,
        desc: str = None,
        spec: DescribeFunctionResponseBodyFunctionSpec = None,
    ):
        self.timing_trigger_config = timing_trigger_config
        self.http_trigger_path = http_trigger_path
        self.created_at = created_at
        self.name = name
        self.modified_at = modified_at
        self.desc = desc
        self.spec = spec

    def validate(self):
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timing_trigger_config is not None:
            result['TimingTriggerConfig'] = self.timing_trigger_config
        if self.http_trigger_path is not None:
            result['HttpTriggerPath'] = self.http_trigger_path
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.name is not None:
            result['Name'] = self.name
        if self.modified_at is not None:
            result['ModifiedAt'] = self.modified_at
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TimingTriggerConfig') is not None:
            self.timing_trigger_config = m.get('TimingTriggerConfig')
        if m.get('HttpTriggerPath') is not None:
            self.http_trigger_path = m.get('HttpTriggerPath')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ModifiedAt') is not None:
            self.modified_at = m.get('ModifiedAt')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Spec') is not None:
            temp_model = DescribeFunctionResponseBodyFunctionSpec()
            self.spec = temp_model.from_map(m['Spec'])
        return self


class DescribeFunctionResponseBodyDeployment(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        deployment_id: str = None,
        download_signed_url: str = None,
        version_no: str = None,
        modified_at: str = None,
    ):
        self.created_at = created_at
        self.deployment_id = deployment_id
        self.download_signed_url = download_signed_url
        self.version_no = version_no
        self.modified_at = modified_at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.deployment_id is not None:
            result['DeploymentId'] = self.deployment_id
        if self.download_signed_url is not None:
            result['DownloadSignedUrl'] = self.download_signed_url
        if self.version_no is not None:
            result['VersionNo'] = self.version_no
        if self.modified_at is not None:
            result['ModifiedAt'] = self.modified_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('DeploymentId') is not None:
            self.deployment_id = m.get('DeploymentId')
        if m.get('DownloadSignedUrl') is not None:
            self.download_signed_url = m.get('DownloadSignedUrl')
        if m.get('VersionNo') is not None:
            self.version_no = m.get('VersionNo')
        if m.get('ModifiedAt') is not None:
            self.modified_at = m.get('ModifiedAt')
        return self


class DescribeFunctionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        function: DescribeFunctionResponseBodyFunction = None,
        deployment: DescribeFunctionResponseBodyDeployment = None,
    ):
        self.request_id = request_id
        self.function = function
        self.deployment = deployment

    def validate(self):
        if self.function:
            self.function.validate()
        if self.deployment:
            self.deployment.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.function is not None:
            result['Function'] = self.function.to_map()
        if self.deployment is not None:
            result['Deployment'] = self.deployment.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Function') is not None:
            temp_model = DescribeFunctionResponseBodyFunction()
            self.function = temp_model.from_map(m['Function'])
        if m.get('Deployment') is not None:
            temp_model = DescribeFunctionResponseBodyDeployment()
            self.deployment = temp_model.from_map(m['Deployment'])
        return self


class DescribeFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFunctionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenWebHostingServiceRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
    ):
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class OpenWebHostingServiceResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class OpenWebHostingServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OpenWebHostingServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OpenWebHostingServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSmsSignRequest(TeaModel):
    def __init__(
        self,
        sign_id: str = None,
        space_id: str = None,
    ):
        self.sign_id = sign_id
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sign_id is not None:
            result['SignId'] = self.sign_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SignId') is not None:
            self.sign_id = m.get('SignId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DescribeSmsSignResponseBody(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        update_time: str = None,
        request_id: str = None,
        remark: str = None,
        create_time: str = None,
        sign_name: str = None,
    ):
        self.space_id = space_id
        self.update_time = update_time
        self.request_id = request_id
        self.remark = remark
        self.create_time = create_time
        self.sign_name = sign_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        return self


class DescribeSmsSignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSmsSignResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSmsSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAvailableCertificatesRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        domain: str = None,
    ):
        self.space_id = space_id
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class ListAvailableCertificatesResponseBodyData(TeaModel):
    def __init__(
        self,
        name: str = None,
        id: str = None,
        status_code: str = None,
    ):
        self.name = name
        self.id = id
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        return self


class ListAvailableCertificatesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[ListAvailableCertificatesResponseBodyData] = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAvailableCertificatesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class ListAvailableCertificatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAvailableCertificatesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListAvailableCertificatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOpenPlatformConfigRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        platform: str = None,
    ):
        self.space_id = space_id
        self.platform = platform

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.platform is not None:
            result['Platform'] = self.platform
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        return self


class ListOpenPlatformConfigResponseBodySecretList(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        app_secret: str = None,
        public_cert: str = None,
        app_cert: str = None,
        private_key: str = None,
        app_id: str = None,
        root_cert: str = None,
        public_key: str = None,
        platform: str = None,
        sign_mode: str = None,
    ):
        self.space_id = space_id
        self.app_secret = app_secret
        self.public_cert = public_cert
        self.app_cert = app_cert
        self.private_key = private_key
        self.app_id = app_id
        self.root_cert = root_cert
        self.public_key = public_key
        self.platform = platform
        self.sign_mode = sign_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.public_cert is not None:
            result['PublicCert'] = self.public_cert
        if self.app_cert is not None:
            result['AppCert'] = self.app_cert
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.root_cert is not None:
            result['RootCert'] = self.root_cert
        if self.public_key is not None:
            result['PublicKey'] = self.public_key
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.sign_mode is not None:
            result['SignMode'] = self.sign_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('PublicCert') is not None:
            self.public_cert = m.get('PublicCert')
        if m.get('AppCert') is not None:
            self.app_cert = m.get('AppCert')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RootCert') is not None:
            self.root_cert = m.get('RootCert')
        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('SignMode') is not None:
            self.sign_mode = m.get('SignMode')
        return self


class ListOpenPlatformConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        secret_list: List[ListOpenPlatformConfigResponseBodySecretList] = None,
    ):
        self.request_id = request_id
        self.secret_list = secret_list

    def validate(self):
        if self.secret_list:
            for k in self.secret_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SecretList'] = []
        if self.secret_list is not None:
            for k in self.secret_list:
                result['SecretList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.secret_list = []
        if m.get('SecretList') is not None:
            for k in m.get('SecretList'):
                temp_model = ListOpenPlatformConfigResponseBodySecretList()
                self.secret_list.append(temp_model.from_map(k))
        return self


class ListOpenPlatformConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListOpenPlatformConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListOpenPlatformConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyWebHostingConfigRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        index_path: str = None,
        error_path: str = None,
        allowed_ips: str = None,
    ):
        self.space_id = space_id
        self.index_path = index_path
        self.error_path = error_path
        self.allowed_ips = allowed_ips

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.index_path is not None:
            result['IndexPath'] = self.index_path
        if self.error_path is not None:
            result['ErrorPath'] = self.error_path
        if self.allowed_ips is not None:
            result['AllowedIps'] = self.allowed_ips
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('IndexPath') is not None:
            self.index_path = m.get('IndexPath')
        if m.get('ErrorPath') is not None:
            self.error_path = m.get('ErrorPath')
        if m.get('AllowedIps') is not None:
            self.allowed_ips = m.get('AllowedIps')
        return self


class ModifyWebHostingConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ModifyWebHostingConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ModifyWebHostingConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyWebHostingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSmsSignRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        sign_id: str = None,
    ):
        self.space_id = space_id
        self.sign_id = sign_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.sign_id is not None:
            result['SignId'] = self.sign_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('SignId') is not None:
            self.sign_id = m.get('SignId')
        return self


class DeleteSmsSignResponseBody(TeaModel):
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


class DeleteSmsSignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSmsSignResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSmsSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSmsOpenStatusResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        request_id: str = None,
        is_authorized: bool = None,
    ):
        self.status = status
        self.request_id = request_id
        self.is_authorized = is_authorized

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.is_authorized is not None:
            result['IsAuthorized'] = self.is_authorized
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IsAuthorized') is not None:
            self.is_authorized = m.get('IsAuthorized')
        return self


class DescribeSmsOpenStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSmsOpenStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSmsOpenStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSpaceRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
    ):
        self.page_num = page_num
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListSpaceResponseBodySpaces(TeaModel):
    def __init__(
        self,
        status: str = None,
        gmt_create: int = None,
        space_id: str = None,
        name: str = None,
        desc: str = None,
    ):
        self.status = status
        self.gmt_create = gmt_create
        self.space_id = space_id
        self.name = name
        self.desc = desc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.name is not None:
            result['Name'] = self.name
        if self.desc is not None:
            result['Desc'] = self.desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        return self


class ListSpaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        gmt_create: str = None,
        count: int = None,
        spaces: List[ListSpaceResponseBodySpaces] = None,
    ):
        self.request_id = request_id
        self.gmt_create = gmt_create
        self.count = count
        self.spaces = spaces

    def validate(self):
        if self.spaces:
            for k in self.spaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.count is not None:
            result['Count'] = self.count
        result['Spaces'] = []
        if self.spaces is not None:
            for k in self.spaces:
                result['Spaces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.spaces = []
        if m.get('Spaces') is not None:
            for k in m.get('Spaces'):
                temp_model = ListSpaceResponseBodySpaces()
                self.spaces.append(temp_model.from_map(k))
        return self


class ListSpaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSpaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSpaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDBCollectionRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        body: str = None,
    ):
        self.space_id = space_id
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.body is not None:
            result['Body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        return self


class DeleteDBCollectionResponseBody(TeaModel):
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


class DeleteDBCollectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDBCollectionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDBCollectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFunctionDeploymentRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        space_id: str = None,
    ):
        self.name = name
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class CreateFunctionDeploymentResponseBody(TeaModel):
    def __init__(
        self,
        upload_signed_url: str = None,
        deployment_id: str = None,
        request_id: str = None,
    ):
        self.upload_signed_url = upload_signed_url
        self.deployment_id = deployment_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.upload_signed_url is not None:
            result['UploadSignedUrl'] = self.upload_signed_url
        if self.deployment_id is not None:
            result['DeploymentId'] = self.deployment_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UploadSignedUrl') is not None:
            self.upload_signed_url = m.get('UploadSignedUrl')
        if m.get('DeploymentId') is not None:
            self.deployment_id = m.get('DeploymentId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFunctionDeploymentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateFunctionDeploymentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateFunctionDeploymentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWebHostingUploadCredentialRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        file_path: str = None,
    ):
        self.space_id = space_id
        self.file_path = file_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        return self


class GetWebHostingUploadCredentialResponseBodyData(TeaModel):
    def __init__(
        self,
        file_path: str = None,
        signature: str = None,
        policy: str = None,
        security_token: str = None,
        expired_time: int = None,
        endpoint: str = None,
        access_key_id: str = None,
    ):
        self.file_path = file_path
        self.signature = signature
        self.policy = policy
        self.security_token = security_token
        self.expired_time = expired_time
        self.endpoint = endpoint
        self.access_key_id = access_key_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.security_token is not None:
            result['SecurityToken'] = self.security_token
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('SecurityToken') is not None:
            self.security_token = m.get('SecurityToken')
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        return self


class GetWebHostingUploadCredentialResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetWebHostingUploadCredentialResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetWebHostingUploadCredentialResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetWebHostingUploadCredentialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetWebHostingUploadCredentialResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetWebHostingUploadCredentialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionDeploymentRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        name: str = None,
        space_id: str = None,
        status: str = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.name = name
        self.space_id = space_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.name is not None:
            result['Name'] = self.name
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListFunctionDeploymentResponseBodyPaginator(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
        page_count: int = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.total = total
        self.page_count = page_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        return self


class ListFunctionDeploymentResponseBodyDataListStatus(TeaModel):
    def __init__(
        self,
        status: str = None,
        label: str = None,
    ):
        self.status = status
        self.label = label

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.label is not None:
            result['Label'] = self.label
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Label') is not None:
            self.label = m.get('Label')
        return self


class ListFunctionDeploymentResponseBodyDataList(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        deployment_id: str = None,
        download_signed_url: str = None,
        version_no: str = None,
        modified_at: str = None,
        status: ListFunctionDeploymentResponseBodyDataListStatus = None,
    ):
        self.created_at = created_at
        self.deployment_id = deployment_id
        self.download_signed_url = download_signed_url
        self.version_no = version_no
        self.modified_at = modified_at
        self.status = status

    def validate(self):
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.deployment_id is not None:
            result['DeploymentId'] = self.deployment_id
        if self.download_signed_url is not None:
            result['DownloadSignedUrl'] = self.download_signed_url
        if self.version_no is not None:
            result['VersionNo'] = self.version_no
        if self.modified_at is not None:
            result['ModifiedAt'] = self.modified_at
        if self.status is not None:
            result['Status'] = self.status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('DeploymentId') is not None:
            self.deployment_id = m.get('DeploymentId')
        if m.get('DownloadSignedUrl') is not None:
            self.download_signed_url = m.get('DownloadSignedUrl')
        if m.get('VersionNo') is not None:
            self.version_no = m.get('VersionNo')
        if m.get('ModifiedAt') is not None:
            self.modified_at = m.get('ModifiedAt')
        if m.get('Status') is not None:
            temp_model = ListFunctionDeploymentResponseBodyDataListStatus()
            self.status = temp_model.from_map(m['Status'])
        return self


class ListFunctionDeploymentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        paginator: ListFunctionDeploymentResponseBodyPaginator = None,
        data_list: List[ListFunctionDeploymentResponseBodyDataList] = None,
    ):
        self.request_id = request_id
        self.paginator = paginator
        self.data_list = data_list

    def validate(self):
        if self.paginator:
            self.paginator.validate()
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.paginator is not None:
            result['Paginator'] = self.paginator.to_map()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Paginator') is not None:
            temp_model = ListFunctionDeploymentResponseBodyPaginator()
            self.paginator = temp_model.from_map(m['Paginator'])
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = ListFunctionDeploymentResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        return self


class ListFunctionDeploymentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFunctionDeploymentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFunctionDeploymentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddDingtalkOpenPlatformConfigRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_secret: str = None,
        space_id: str = None,
    ):
        self.app_id = app_id
        self.app_secret = app_secret
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class AddDingtalkOpenPlatformConfigResponseBody(TeaModel):
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


class AddDingtalkOpenPlatformConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddDingtalkOpenPlatformConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddDingtalkOpenPlatformConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBRestoreTaskRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        backup_id: str = None,
        origin_collections: str = None,
        new_collections: str = None,
    ):
        self.space_id = space_id
        self.backup_id = backup_id
        self.origin_collections = origin_collections
        self.new_collections = new_collections

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.origin_collections is not None:
            result['OriginCollections'] = self.origin_collections
        if self.new_collections is not None:
            result['NewCollections'] = self.new_collections
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('OriginCollections') is not None:
            self.origin_collections = m.get('OriginCollections')
        if m.get('NewCollections') is not None:
            self.new_collections = m.get('NewCollections')
        return self


class CreateDBRestoreTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateDBRestoreTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDBRestoreTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDBRestoreTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachWebHostingCertificateRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        domain: str = None,
        cert_type: str = None,
        cert_name: str = None,
        server_certificate: str = None,
        private_key: str = None,
    ):
        self.space_id = space_id
        self.domain = domain
        self.cert_type = cert_type
        self.cert_name = cert_name
        self.server_certificate = server_certificate
        self.private_key = private_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.cert_type is not None:
            result['CertType'] = self.cert_type
        if self.cert_name is not None:
            result['CertName'] = self.cert_name
        if self.server_certificate is not None:
            result['ServerCertificate'] = self.server_certificate
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('CertType') is not None:
            self.cert_type = m.get('CertType')
        if m.get('CertName') is not None:
            self.cert_name = m.get('CertName')
        if m.get('ServerCertificate') is not None:
            self.server_certificate = m.get('ServerCertificate')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        return self


class AttachWebHostingCertificateResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AttachWebHostingCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AttachWebHostingCertificateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AttachWebHostingCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFileRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        page_num: int = None,
        page_size: int = None,
        keyword: str = None,
    ):
        self.space_id = space_id
        self.page_num = page_num
        self.page_size = page_size
        self.keyword = keyword

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        return self


class ListFileResponseBodyPaginator(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
        page_count: int = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.total = total
        self.page_count = page_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        return self


class ListFileResponseBodyDataList(TeaModel):
    def __init__(
        self,
        type: str = None,
        size: int = None,
        gmt_create: str = None,
        url: str = None,
        gmt_modified: str = None,
        name: str = None,
        id: str = None,
    ):
        self.type = type
        self.size = size
        self.gmt_create = gmt_create
        self.url = url
        self.gmt_modified = gmt_modified
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.size is not None:
            result['Size'] = self.size
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.url is not None:
            result['Url'] = self.url
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListFileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        paginator: ListFileResponseBodyPaginator = None,
        data_list: List[ListFileResponseBodyDataList] = None,
    ):
        self.request_id = request_id
        self.paginator = paginator
        self.data_list = data_list

    def validate(self):
        if self.paginator:
            self.paginator.validate()
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.paginator is not None:
            result['Paginator'] = self.paginator.to_map()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Paginator') is not None:
            temp_model = ListFileResponseBodyPaginator()
            self.paginator = temp_model.from_map(m['Paginator'])
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = ListFileResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        return self


class ListFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDBRestoreTaskStatusRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        task_id: str = None,
    ):
        self.space_id = space_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class QueryDBRestoreTaskStatusResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        failed_count: int = None,
        request_id: str = None,
        detail_message: str = None,
        success_count: int = None,
    ):
        self.status = status
        self.failed_count = failed_count
        self.request_id = request_id
        self.detail_message = detail_message
        self.success_count = success_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.failed_count is not None:
            result['FailedCount'] = self.failed_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.detail_message is not None:
            result['DetailMessage'] = self.detail_message
        if self.success_count is not None:
            result['SuccessCount'] = self.success_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('FailedCount') is not None:
            self.failed_count = m.get('FailedCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DetailMessage') is not None:
            self.detail_message = m.get('DetailMessage')
        if m.get('SuccessCount') is not None:
            self.success_count = m.get('SuccessCount')
        return self


class QueryDBRestoreTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDBRestoreTaskStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryDBRestoreTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyWebHostingDomainOwnerRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        domain: str = None,
        verify_type: str = None,
    ):
        self.space_id = space_id
        self.domain = domain
        self.verify_type = verify_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.verify_type is not None:
            result['VerifyType'] = self.verify_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('VerifyType') is not None:
            self.verify_type = m.get('VerifyType')
        return self


class VerifyWebHostingDomainOwnerResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class VerifyWebHostingDomainOwnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: VerifyWebHostingDomainOwnerResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = VerifyWebHostingDomainOwnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSmsTemplateRequest(TeaModel):
    def __init__(
        self,
        template_code: str = None,
        space_id: str = None,
    ):
        self.template_code = template_code
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DeleteSmsTemplateResponseBody(TeaModel):
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


class DeleteSmsTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteSmsTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteSmsTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDBExportTaskStatusRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        task_id: str = None,
    ):
        self.space_id = space_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class QueryDBExportTaskStatusResponseBody(TeaModel):
    def __init__(
        self,
        exported_count: str = None,
        status: str = None,
        request_id: str = None,
        download_url: str = None,
        detail_message: str = None,
    ):
        self.exported_count = exported_count
        self.status = status
        self.request_id = request_id
        self.download_url = download_url
        self.detail_message = detail_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exported_count is not None:
            result['ExportedCount'] = self.exported_count
        if self.status is not None:
            result['Status'] = self.status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.download_url is not None:
            result['DownloadUrl'] = self.download_url
        if self.detail_message is not None:
            result['DetailMessage'] = self.detail_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExportedCount') is not None:
            self.exported_count = m.get('ExportedCount')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DownloadUrl') is not None:
            self.download_url = m.get('DownloadUrl')
        if m.get('DetailMessage') is not None:
            self.detail_message = m.get('DetailMessage')
        return self


class QueryDBExportTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDBExportTaskStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryDBExportTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBImportTaskRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        collection: str = None,
        file_type: str = None,
        mode: str = None,
    ):
        self.space_id = space_id
        self.collection = collection
        self.file_type = file_type
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.mode is not None:
            result['Mode'] = self.mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        return self


class CreateDBImportTaskResponseBody(TeaModel):
    def __init__(
        self,
        host: str = None,
        expire_time: str = None,
        file_key: str = None,
        access_key_id: str = None,
        signature: str = None,
        request_id: str = None,
        policy: str = None,
        task_id: str = None,
    ):
        self.host = host
        self.expire_time = expire_time
        self.file_key = file_key
        self.access_key_id = access_key_id
        self.signature = signature
        self.request_id = request_id
        self.policy = policy
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.file_key is not None:
            result['FileKey'] = self.file_key
        if self.access_key_id is not None:
            result['AccessKeyId'] = self.access_key_id
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')
        if m.get('AccessKeyId') is not None:
            self.access_key_id = m.get('AccessKeyId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateDBImportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDBImportTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDBImportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckSmsHasAuthorizedToMPSRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
    ):
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class CheckSmsHasAuthorizedToMPSResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        is_authorized: bool = None,
    ):
        self.request_id = request_id
        self.is_authorized = is_authorized

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.is_authorized is not None:
            result['IsAuthorized'] = self.is_authorized
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('IsAuthorized') is not None:
            self.is_authorized = m.get('IsAuthorized')
        return self


class CheckSmsHasAuthorizedToMPSResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckSmsHasAuthorizedToMPSResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckSmsHasAuthorizedToMPSResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeServicePolicyRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        service_name: str = None,
        collection_name: str = None,
    ):
        self.space_id = space_id
        self.service_name = service_name
        self.collection_name = collection_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.collection_name is not None:
            result['CollectionName'] = self.collection_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('CollectionName') is not None:
            self.collection_name = m.get('CollectionName')
        return self


class DescribeServicePolicyResponseBody(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        request_id: str = None,
        policy: str = None,
        policy_name: str = None,
        service_name: str = None,
        collection_name: str = None,
    ):
        self.space_id = space_id
        self.request_id = request_id
        self.policy = policy
        self.policy_name = policy_name
        self.service_name = service_name
        self.collection_name = collection_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.collection_name is not None:
            result['CollectionName'] = self.collection_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('CollectionName') is not None:
            self.collection_name = m.get('CollectionName')
        return self


class DescribeServicePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeServicePolicyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeServicePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSmsTemplatesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        space_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class ListSmsTemplatesResponseBodySmsTemplates(TeaModel):
    def __init__(
        self,
        update_time: str = None,
        template_content: str = None,
        remark: str = None,
        template_code: str = None,
        create_time: str = None,
        template_type: int = None,
        template_name: str = None,
    ):
        self.update_time = update_time
        self.template_content = template_content
        self.remark = remark
        self.template_code = template_code
        self.create_time = create_time
        self.template_type = template_type
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class ListSmsTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        sms_templates: List[ListSmsTemplatesResponseBodySmsTemplates] = None,
    ):
        self.request_id = request_id
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.sms_templates = sms_templates

    def validate(self):
        if self.sms_templates:
            for k in self.sms_templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['SmsTemplates'] = []
        if self.sms_templates is not None:
            for k in self.sms_templates:
                result['SmsTemplates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.sms_templates = []
        if m.get('SmsTemplates') is not None:
            for k in m.get('SmsTemplates'):
                temp_model = ListSmsTemplatesResponseBodySmsTemplates()
                self.sms_templates.append(temp_model.from_map(k))
        return self


class ListSmsTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSmsTemplatesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSmsTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDBBackupCollectionsRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        backup_id: str = None,
    ):
        self.space_id = space_id
        self.backup_id = backup_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        return self


class QueryDBBackupCollectionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        collections: List[str] = None,
    ):
        self.request_id = request_id
        self.collections = collections

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.collections is not None:
            result['Collections'] = self.collections
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Collections') is not None:
            self.collections = m.get('Collections')
        return self


class QueryDBBackupCollectionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDBBackupCollectionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryDBBackupCollectionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryServiceStatusRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        service_name: str = None,
    ):
        self.space_id = space_id
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        return self


class QueryServiceStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        service_status: str = None,
        count: int = None,
    ):
        self.request_id = request_id
        self.service_status = service_status
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class QueryServiceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryServiceStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSpaceClientConfigRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        detail: str = None,
        workspace_id: int = None,
    ):
        self.space_id = space_id
        self.detail = detail
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class DescribeSpaceClientConfigResponseBody(TeaModel):
    def __init__(
        self,
        api_key: str = None,
        space_id: str = None,
        request_id: str = None,
        private_key: str = None,
        endpoint: str = None,
        file_upload_endpoint: str = None,
        name: str = None,
    ):
        self.api_key = api_key
        self.space_id = space_id
        self.request_id = request_id
        self.private_key = private_key
        self.endpoint = endpoint
        self.file_upload_endpoint = file_upload_endpoint
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_key is not None:
            result['ApiKey'] = self.api_key
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint
        if self.file_upload_endpoint is not None:
            result['FileUploadEndpoint'] = self.file_upload_endpoint
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')
        if m.get('FileUploadEndpoint') is not None:
            self.file_upload_endpoint = m.get('FileUploadEndpoint')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeSpaceClientConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSpaceClientConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSpaceClientConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveBuiltinFunctionTemplateRequest(TeaModel):
    def __init__(
        self,
        biz_id: str = None,
        builtin_function_template_category_id: str = None,
        builtin_function_template_profile: str = None,
    ):
        self.biz_id = biz_id
        self.builtin_function_template_category_id = builtin_function_template_category_id
        self.builtin_function_template_profile = builtin_function_template_profile

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.builtin_function_template_category_id is not None:
            result['BuiltinFunctionTemplateCategoryId'] = self.builtin_function_template_category_id
        if self.builtin_function_template_profile is not None:
            result['BuiltinFunctionTemplateProfile'] = self.builtin_function_template_profile
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('BuiltinFunctionTemplateCategoryId') is not None:
            self.builtin_function_template_category_id = m.get('BuiltinFunctionTemplateCategoryId')
        if m.get('BuiltinFunctionTemplateProfile') is not None:
            self.builtin_function_template_profile = m.get('BuiltinFunctionTemplateProfile')
        return self


class SaveBuiltinFunctionTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        builtin_function_template_id: str = None,
    ):
        self.request_id = request_id
        self.builtin_function_template_id = builtin_function_template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.builtin_function_template_id is not None:
            result['BuiltinFunctionTemplateId'] = self.builtin_function_template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BuiltinFunctionTemplateId') is not None:
            self.builtin_function_template_id = m.get('BuiltinFunctionTemplateId')
        return self


class SaveBuiltinFunctionTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SaveBuiltinFunctionTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SaveBuiltinFunctionTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeISVFileUploadSignedUrlRequest(TeaModel):
    def __init__(
        self,
        filename: str = None,
        bucket_name: str = None,
        tenant_id: str = None,
    ):
        self.filename = filename
        self.bucket_name = bucket_name
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filename is not None:
            result['Filename'] = self.filename
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filename') is not None:
            self.filename = m.get('Filename')
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        return self


class DescribeISVFileUploadSignedUrlResponseBody(TeaModel):
    def __init__(
        self,
        sign_url: str = None,
        request_id: str = None,
        id: str = None,
    ):
        self.sign_url = sign_url
        self.request_id = request_id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sign_url is not None:
            result['SignUrl'] = self.sign_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SignUrl') is not None:
            self.sign_url = m.get('SignUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeISVFileUploadSignedUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeISVFileUploadSignedUrlResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeISVFileUploadSignedUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBuiltinFunctionTemplateRequest(TeaModel):
    def __init__(
        self,
        builtin_function_template_category_id: str = None,
    ):
        self.builtin_function_template_category_id = builtin_function_template_category_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.builtin_function_template_category_id is not None:
            result['BuiltinFunctionTemplateCategoryId'] = self.builtin_function_template_category_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuiltinFunctionTemplateCategoryId') is not None:
            self.builtin_function_template_category_id = m.get('BuiltinFunctionTemplateCategoryId')
        return self


class CreateBuiltinFunctionTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        biz_id: str = None,
        artifact_upload_url: str = None,
    ):
        self.request_id = request_id
        self.biz_id = biz_id
        self.artifact_upload_url = artifact_upload_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.biz_id is not None:
            result['BizId'] = self.biz_id
        if self.artifact_upload_url is not None:
            result['ArtifactUploadUrl'] = self.artifact_upload_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')
        if m.get('ArtifactUploadUrl') is not None:
            self.artifact_upload_url = m.get('ArtifactUploadUrl')
        return self


class CreateBuiltinFunctionTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateBuiltinFunctionTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateBuiltinFunctionTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWebHostingStatusRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
    ):
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class GetWebHostingStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
        space_id: str = None,
    ):
        self.status = status
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class GetWebHostingStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetWebHostingStatusResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetWebHostingStatusResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetWebHostingStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetWebHostingStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetWebHostingStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFunctionLogRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        name: str = None,
        space_id: str = None,
        log_request_id: str = None,
        from_date: int = None,
        to_date: int = None,
        status: str = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.name = name
        self.space_id = space_id
        self.log_request_id = log_request_id
        self.from_date = from_date
        self.to_date = to_date
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.name is not None:
            result['Name'] = self.name
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.log_request_id is not None:
            result['LogRequestId'] = self.log_request_id
        if self.from_date is not None:
            result['FromDate'] = self.from_date
        if self.to_date is not None:
            result['ToDate'] = self.to_date
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('LogRequestId') is not None:
            self.log_request_id = m.get('LogRequestId')
        if m.get('FromDate') is not None:
            self.from_date = m.get('FromDate')
        if m.get('ToDate') is not None:
            self.to_date = m.get('ToDate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListFunctionLogResponseBodyPaginator(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        total: int = None,
        page_count: int = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.total = total
        self.page_count = page_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total is not None:
            result['Total'] = self.total
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        return self


class ListFunctionLogResponseBodyDataList(TeaModel):
    def __init__(
        self,
        status: str = None,
        space_id: str = None,
        request_id: str = None,
        function_name: str = None,
        timestamps: List[str] = None,
        contents: List[str] = None,
        levels: List[str] = None,
    ):
        self.status = status
        self.space_id = space_id
        self.request_id = request_id
        self.function_name = function_name
        self.timestamps = timestamps
        self.contents = contents
        self.levels = levels

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.function_name is not None:
            result['FunctionName'] = self.function_name
        if self.timestamps is not None:
            result['Timestamps'] = self.timestamps
        if self.contents is not None:
            result['Contents'] = self.contents
        if self.levels is not None:
            result['Levels'] = self.levels
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')
        if m.get('Timestamps') is not None:
            self.timestamps = m.get('Timestamps')
        if m.get('Contents') is not None:
            self.contents = m.get('Contents')
        if m.get('Levels') is not None:
            self.levels = m.get('Levels')
        return self


class ListFunctionLogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        paginator: ListFunctionLogResponseBodyPaginator = None,
        data_list: List[ListFunctionLogResponseBodyDataList] = None,
    ):
        self.request_id = request_id
        self.paginator = paginator
        self.data_list = data_list

    def validate(self):
        if self.paginator:
            self.paginator.validate()
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.paginator is not None:
            result['Paginator'] = self.paginator.to_map()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Paginator') is not None:
            temp_model = ListFunctionLogResponseBodyPaginator()
            self.paginator = temp_model.from_map(m['Paginator'])
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = ListFunctionLogResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k))
        return self


class ListFunctionLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFunctionLogResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListFunctionLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWebHostingFilesRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        prefix: str = None,
        marker: str = None,
        page_size: int = None,
    ):
        self.space_id = space_id
        self.prefix = prefix
        self.marker = marker
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.prefix is not None:
            result['Prefix'] = self.prefix
        if self.marker is not None:
            result['Marker'] = self.marker
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')
        if m.get('Marker') is not None:
            self.marker = m.get('Marker')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListWebHostingFilesResponseBodyDataWebHostingFiles(TeaModel):
    def __init__(
        self,
        file_path: str = None,
        content_type: str = None,
        etag: str = None,
        size: int = None,
        last_modified_time: int = None,
        signed_url: str = None,
    ):
        self.file_path = file_path
        self.content_type = content_type
        self.etag = etag
        self.size = size
        self.last_modified_time = last_modified_time
        self.signed_url = signed_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.etag is not None:
            result['ETag'] = self.etag
        if self.size is not None:
            result['Size'] = self.size
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.signed_url is not None:
            result['SignedUrl'] = self.signed_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('ETag') is not None:
            self.etag = m.get('ETag')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('SignedUrl') is not None:
            self.signed_url = m.get('SignedUrl')
        return self


class ListWebHostingFilesResponseBodyData(TeaModel):
    def __init__(
        self,
        next_marker: str = None,
        count: int = None,
        web_hosting_files: List[ListWebHostingFilesResponseBodyDataWebHostingFiles] = None,
    ):
        self.next_marker = next_marker
        self.count = count
        self.web_hosting_files = web_hosting_files

    def validate(self):
        if self.web_hosting_files:
            for k in self.web_hosting_files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker
        if self.count is not None:
            result['Count'] = self.count
        result['WebHostingFiles'] = []
        if self.web_hosting_files is not None:
            for k in self.web_hosting_files:
                result['WebHostingFiles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.web_hosting_files = []
        if m.get('WebHostingFiles') is not None:
            for k in m.get('WebHostingFiles'):
                temp_model = ListWebHostingFilesResponseBodyDataWebHostingFiles()
                self.web_hosting_files.append(temp_model.from_map(k))
        return self


class ListWebHostingFilesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: ListWebHostingFilesResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = ListWebHostingFilesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class ListWebHostingFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListWebHostingFilesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListWebHostingFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeFileRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        space_id: str = None,
    ):
        self.id = id
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DescribeFileResponseBody(TeaModel):
    def __init__(
        self,
        type: str = None,
        url: str = None,
        gmt_modified: str = None,
        request_id: str = None,
        size: float = None,
        gmt_create: str = None,
        name: str = None,
        id: str = None,
    ):
        self.type = type
        self.url = url
        self.gmt_modified = gmt_modified
        self.request_id = request_id
        self.size = size
        self.gmt_create = gmt_create
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DescribeFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeFileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveWebHostingFileRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        source_file_path: str = None,
        target_file_path: str = None,
    ):
        self.space_id = space_id
        self.source_file_path = source_file_path
        self.target_file_path = target_file_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.source_file_path is not None:
            result['SourceFilePath'] = self.source_file_path
        if self.target_file_path is not None:
            result['TargetFilePath'] = self.target_file_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('SourceFilePath') is not None:
            self.source_file_path = m.get('SourceFilePath')
        if m.get('TargetFilePath') is not None:
            self.target_file_path = m.get('TargetFilePath')
        return self


class MoveWebHostingFileResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class MoveWebHostingFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: MoveWebHostingFileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = MoveWebHostingFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSmsTemplateRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        template_type: int = None,
        template_name: str = None,
        template_content: str = None,
        remark: str = None,
    ):
        self.space_id = space_id
        self.template_type = template_type
        self.template_name = template_name
        self.template_content = template_content
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class CreateSmsTemplateResponseBody(TeaModel):
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


class CreateSmsTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSmsTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSmsTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSmsTemplateStatusRequest(TeaModel):
    def __init__(
        self,
        template_codes: str = None,
        space_id: str = None,
    ):
        self.template_codes = template_codes
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_codes is not None:
            result['TemplateCodes'] = self.template_codes
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateCodes') is not None:
            self.template_codes = m.get('TemplateCodes')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DescribeSmsTemplateStatusResponseBodyTemplateStatuses(TeaModel):
    def __init__(
        self,
        template_code: str = None,
        reason: str = None,
        template_status: str = None,
    ):
        self.template_code = template_code
        self.reason = reason
        self.template_status = template_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.template_status is not None:
            result['TemplateStatus'] = self.template_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('TemplateStatus') is not None:
            self.template_status = m.get('TemplateStatus')
        return self


class DescribeSmsTemplateStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template_statuses: List[DescribeSmsTemplateStatusResponseBodyTemplateStatuses] = None,
    ):
        self.request_id = request_id
        self.template_statuses = template_statuses

    def validate(self):
        if self.template_statuses:
            for k in self.template_statuses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TemplateStatuses'] = []
        if self.template_statuses is not None:
            for k in self.template_statuses:
                result['TemplateStatuses'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.template_statuses = []
        if m.get('TemplateStatuses') is not None:
            for k in m.get('TemplateStatuses'):
                temp_model = DescribeSmsTemplateStatusResponseBodyTemplateStatuses()
                self.template_statuses.append(temp_model.from_map(k))
        return self


class DescribeSmsTemplateStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSmsTemplateStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSmsTemplateStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindWebHostingCustomDomainRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        custom_domain: str = None,
    ):
        self.space_id = space_id
        self.custom_domain = custom_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.custom_domain is not None:
            result['CustomDomain'] = self.custom_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('CustomDomain') is not None:
            self.custom_domain = m.get('CustomDomain')
        return self


class BindWebHostingCustomDomainResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BindWebHostingCustomDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BindWebHostingCustomDomainResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BindWebHostingCustomDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFunctionRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        desc: str = None,
        space_id: str = None,
        runtime: str = None,
    ):
        self.name = name
        self.desc = desc
        self.space_id = space_id
        self.runtime = runtime

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.runtime is not None:
            result['Runtime'] = self.runtime
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Runtime') is not None:
            self.runtime = m.get('Runtime')
        return self


class CreateFunctionResponseBodySpec(TeaModel):
    def __init__(
        self,
        timeout: str = None,
        runtime: str = None,
        instance_concurrency: str = None,
        memory: str = None,
    ):
        self.timeout = timeout
        self.runtime = runtime
        self.instance_concurrency = instance_concurrency
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.runtime is not None:
            result['Runtime'] = self.runtime
        if self.instance_concurrency is not None:
            result['InstanceConcurrency'] = self.instance_concurrency
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('Runtime') is not None:
            self.runtime = m.get('Runtime')
        if m.get('InstanceConcurrency') is not None:
            self.instance_concurrency = m.get('InstanceConcurrency')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class CreateFunctionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        created_at: str = None,
        name: str = None,
        modified_at: str = None,
        desc: str = None,
        spec: CreateFunctionResponseBodySpec = None,
    ):
        self.request_id = request_id
        self.created_at = created_at
        self.name = name
        self.modified_at = modified_at
        self.desc = desc
        self.spec = spec

    def validate(self):
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.name is not None:
            result['Name'] = self.name
        if self.modified_at is not None:
            result['ModifiedAt'] = self.modified_at
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ModifiedAt') is not None:
            self.modified_at = m.get('ModifiedAt')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Spec') is not None:
            temp_model = CreateFunctionResponseBodySpec()
            self.spec = temp_model.from_map(m['Spec'])
        return self


class CreateFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateFunctionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDingtalkOpenPlatformConfigRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        space_id: str = None,
    ):
        self.app_id = app_id
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DeleteDingtalkOpenPlatformConfigResponseBody(TeaModel):
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


class DeleteDingtalkOpenPlatformConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteDingtalkOpenPlatformConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteDingtalkOpenPlatformConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExtensionsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListExtensionsResponseBodyExtensions(TeaModel):
    def __init__(
        self,
        extension_documentation_link: str = None,
        extension_id: str = None,
        extension_desc: str = None,
        extension_name: str = None,
        enabled: str = None,
    ):
        self.extension_documentation_link = extension_documentation_link
        self.extension_id = extension_id
        self.extension_desc = extension_desc
        self.extension_name = extension_name
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extension_documentation_link is not None:
            result['ExtensionDocumentationLink'] = self.extension_documentation_link
        if self.extension_id is not None:
            result['ExtensionId'] = self.extension_id
        if self.extension_desc is not None:
            result['ExtensionDesc'] = self.extension_desc
        if self.extension_name is not None:
            result['ExtensionName'] = self.extension_name
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtensionDocumentationLink') is not None:
            self.extension_documentation_link = m.get('ExtensionDocumentationLink')
        if m.get('ExtensionId') is not None:
            self.extension_id = m.get('ExtensionId')
        if m.get('ExtensionDesc') is not None:
            self.extension_desc = m.get('ExtensionDesc')
        if m.get('ExtensionName') is not None:
            self.extension_name = m.get('ExtensionName')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        return self


class ListExtensionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        extensions: List[ListExtensionsResponseBodyExtensions] = None,
    ):
        self.request_id = request_id
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.extensions = extensions

    def validate(self):
        if self.extensions:
            for k in self.extensions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Extensions'] = []
        if self.extensions is not None:
            for k in self.extensions:
                result['Extensions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.extensions = []
        if m.get('Extensions') is not None:
            for k in m.get('Extensions'):
                temp_model = ListExtensionsResponseBodyExtensions()
                self.extensions.append(temp_model.from_map(k))
        return self


class ListExtensionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListExtensionsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListExtensionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableSmsServiceResponseBody(TeaModel):
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


class EnableSmsServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableSmsServiceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableSmsServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReleaseBuiltinFunctionTemplateRequest(TeaModel):
    def __init__(
        self,
        builtin_function_template_id: str = None,
    ):
        self.builtin_function_template_id = builtin_function_template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.builtin_function_template_id is not None:
            result['BuiltinFunctionTemplateId'] = self.builtin_function_template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuiltinFunctionTemplateId') is not None:
            self.builtin_function_template_id = m.get('BuiltinFunctionTemplateId')
        return self


class ReleaseBuiltinFunctionTemplateResponseBody(TeaModel):
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


class ReleaseBuiltinFunctionTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ReleaseBuiltinFunctionTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ReleaseBuiltinFunctionTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSmsSignRequest(TeaModel):
    def __init__(
        self,
        sign_name: str = None,
        remark: str = None,
        space_id: str = None,
    ):
        self.sign_name = sign_name
        self.remark = remark
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class CreateSmsSignResponseBody(TeaModel):
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


class CreateSmsSignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSmsSignResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateSmsSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFunctionRequest(TeaModel):
    def __init__(
        self,
        desc: str = None,
        name: str = None,
        space_id: str = None,
        memory: int = None,
        timeout: int = None,
        http_trigger_path: str = None,
        timing_trigger_config: str = None,
        instance_concurrency: int = None,
        runtime: str = None,
    ):
        self.desc = desc
        self.name = name
        self.space_id = space_id
        self.memory = memory
        self.timeout = timeout
        self.http_trigger_path = http_trigger_path
        self.timing_trigger_config = timing_trigger_config
        self.instance_concurrency = instance_concurrency
        self.runtime = runtime

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.name is not None:
            result['Name'] = self.name
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.memory is not None:
            result['Memory'] = self.memory
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.http_trigger_path is not None:
            result['HttpTriggerPath'] = self.http_trigger_path
        if self.timing_trigger_config is not None:
            result['TimingTriggerConfig'] = self.timing_trigger_config
        if self.instance_concurrency is not None:
            result['InstanceConcurrency'] = self.instance_concurrency
        if self.runtime is not None:
            result['Runtime'] = self.runtime
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('HttpTriggerPath') is not None:
            self.http_trigger_path = m.get('HttpTriggerPath')
        if m.get('TimingTriggerConfig') is not None:
            self.timing_trigger_config = m.get('TimingTriggerConfig')
        if m.get('InstanceConcurrency') is not None:
            self.instance_concurrency = m.get('InstanceConcurrency')
        if m.get('Runtime') is not None:
            self.runtime = m.get('Runtime')
        return self


class UpdateFunctionResponseBodySpec(TeaModel):
    def __init__(
        self,
        timeout: str = None,
        runtime: str = None,
        instance_concurrency: int = None,
        memory: str = None,
    ):
        self.timeout = timeout
        self.runtime = runtime
        self.instance_concurrency = instance_concurrency
        self.memory = memory

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.runtime is not None:
            result['Runtime'] = self.runtime
        if self.instance_concurrency is not None:
            result['InstanceConcurrency'] = self.instance_concurrency
        if self.memory is not None:
            result['Memory'] = self.memory
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('Runtime') is not None:
            self.runtime = m.get('Runtime')
        if m.get('InstanceConcurrency') is not None:
            self.instance_concurrency = m.get('InstanceConcurrency')
        if m.get('Memory') is not None:
            self.memory = m.get('Memory')
        return self


class UpdateFunctionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        timing_trigger_config: str = None,
        http_trigger_path: str = None,
        created_at: str = None,
        name: str = None,
        modified_at: str = None,
        desc: str = None,
        spec: UpdateFunctionResponseBodySpec = None,
    ):
        self.request_id = request_id
        self.timing_trigger_config = timing_trigger_config
        self.http_trigger_path = http_trigger_path
        self.created_at = created_at
        self.name = name
        self.modified_at = modified_at
        self.desc = desc
        self.spec = spec

    def validate(self):
        if self.spec:
            self.spec.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.timing_trigger_config is not None:
            result['TimingTriggerConfig'] = self.timing_trigger_config
        if self.http_trigger_path is not None:
            result['HttpTriggerPath'] = self.http_trigger_path
        if self.created_at is not None:
            result['CreatedAt'] = self.created_at
        if self.name is not None:
            result['Name'] = self.name
        if self.modified_at is not None:
            result['ModifiedAt'] = self.modified_at
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.spec is not None:
            result['Spec'] = self.spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TimingTriggerConfig') is not None:
            self.timing_trigger_config = m.get('TimingTriggerConfig')
        if m.get('HttpTriggerPath') is not None:
            self.http_trigger_path = m.get('HttpTriggerPath')
        if m.get('CreatedAt') is not None:
            self.created_at = m.get('CreatedAt')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ModifiedAt') is not None:
            self.modified_at = m.get('ModifiedAt')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Spec') is not None:
            temp_model = UpdateFunctionResponseBodySpec()
            self.spec = temp_model.from_map(m['Spec'])
        return self


class UpdateFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateFunctionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateHttpTriggerConfigRequest(TeaModel):
    def __init__(
        self,
        enable_service: bool = None,
        space_id: str = None,
        custom_domain: str = None,
        custom_domain_certificate: str = None,
        custom_domain_private_key: str = None,
    ):
        self.enable_service = enable_service
        self.space_id = space_id
        self.custom_domain = custom_domain
        self.custom_domain_certificate = custom_domain_certificate
        self.custom_domain_private_key = custom_domain_private_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_service is not None:
            result['EnableService'] = self.enable_service
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.custom_domain is not None:
            result['CustomDomain'] = self.custom_domain
        if self.custom_domain_certificate is not None:
            result['CustomDomainCertificate'] = self.custom_domain_certificate
        if self.custom_domain_private_key is not None:
            result['CustomDomainPrivateKey'] = self.custom_domain_private_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableService') is not None:
            self.enable_service = m.get('EnableService')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('CustomDomain') is not None:
            self.custom_domain = m.get('CustomDomain')
        if m.get('CustomDomainCertificate') is not None:
            self.custom_domain_certificate = m.get('CustomDomainCertificate')
        if m.get('CustomDomainPrivateKey') is not None:
            self.custom_domain_private_key = m.get('CustomDomainPrivateKey')
        return self


class UpdateHttpTriggerConfigResponseBody(TeaModel):
    def __init__(
        self,
        enable_service: bool = None,
        custom_domain_cname: str = None,
        request_id: str = None,
        default_endpoint: str = None,
        custom_domain_certificate_info: str = None,
        custom_domain: str = None,
    ):
        self.enable_service = enable_service
        self.custom_domain_cname = custom_domain_cname
        self.request_id = request_id
        self.default_endpoint = default_endpoint
        self.custom_domain_certificate_info = custom_domain_certificate_info
        self.custom_domain = custom_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_service is not None:
            result['EnableService'] = self.enable_service
        if self.custom_domain_cname is not None:
            result['CustomDomainCname'] = self.custom_domain_cname
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.default_endpoint is not None:
            result['DefaultEndpoint'] = self.default_endpoint
        if self.custom_domain_certificate_info is not None:
            result['CustomDomainCertificateInfo'] = self.custom_domain_certificate_info
        if self.custom_domain is not None:
            result['CustomDomain'] = self.custom_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableService') is not None:
            self.enable_service = m.get('EnableService')
        if m.get('CustomDomainCname') is not None:
            self.custom_domain_cname = m.get('CustomDomainCname')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DefaultEndpoint') is not None:
            self.default_endpoint = m.get('DefaultEndpoint')
        if m.get('CustomDomainCertificateInfo') is not None:
            self.custom_domain_certificate_info = m.get('CustomDomainCertificateInfo')
        if m.get('CustomDomain') is not None:
            self.custom_domain = m.get('CustomDomain')
        return self


class UpdateHttpTriggerConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateHttpTriggerConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateHttpTriggerConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetServerSecretRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
    ):
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class ResetServerSecretResponseBody(TeaModel):
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


class ResetServerSecretResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResetServerSecretResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ResetServerSecretResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWebHostingDomainVerificationContentRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        domain: str = None,
    ):
        self.space_id = space_id
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class GetWebHostingDomainVerificationContentResponseBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
        domain: str = None,
    ):
        self.content = content
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class GetWebHostingDomainVerificationContentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetWebHostingDomainVerificationContentResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetWebHostingDomainVerificationContentResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetWebHostingDomainVerificationContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetWebHostingDomainVerificationContentResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetWebHostingDomainVerificationContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDingtalkOpenPlatformConfigRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_secret: str = None,
        space_id: str = None,
    ):
        self.app_id = app_id
        self.app_secret = app_secret
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class UpdateDingtalkOpenPlatformConfigResponseBody(TeaModel):
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


class UpdateDingtalkOpenPlatformConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateDingtalkOpenPlatformConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateDingtalkOpenPlatformConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckMpServerlessRoleExistsRequest(TeaModel):
    def __init__(
        self,
        role_name: str = None,
    ):
        self.role_name = role_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_name is not None:
            result['RoleName'] = self.role_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoleName') is not None:
            self.role_name = m.get('RoleName')
        return self


class CheckMpServerlessRoleExistsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        exists: bool = None,
    ):
        self.request_id = request_id
        self.exists = exists

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.exists is not None:
            result['Exists'] = self.exists
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Exists') is not None:
            self.exists = m.get('Exists')
        return self


class CheckMpServerlessRoleExistsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckMpServerlessRoleExistsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CheckMpServerlessRoleExistsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableExtensionRequest(TeaModel):
    def __init__(
        self,
        extension_id: str = None,
    ):
        self.extension_id = extension_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extension_id is not None:
            result['ExtensionId'] = self.extension_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtensionId') is not None:
            self.extension_id = m.get('ExtensionId')
        return self


class EnableExtensionResponseBody(TeaModel):
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


class EnableExtensionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: EnableExtensionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableExtensionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSmsSignsForAccountRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        space_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class ListSmsSignsForAccountResponseBodySmsSigns(TeaModel):
    def __init__(
        self,
        sign_name: str = None,
    ):
        self.sign_name = sign_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        return self


class ListSmsSignsForAccountResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        sms_signs: List[ListSmsSignsForAccountResponseBodySmsSigns] = None,
    ):
        self.request_id = request_id
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.sms_signs = sms_signs

    def validate(self):
        if self.sms_signs:
            for k in self.sms_signs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['SmsSigns'] = []
        if self.sms_signs is not None:
            for k in self.sms_signs:
                result['SmsSigns'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.sms_signs = []
        if m.get('SmsSigns') is not None:
            for k in m.get('SmsSigns'):
                temp_model = ListSmsSignsForAccountResponseBodySmsSigns()
                self.sms_signs.append(temp_model.from_map(k))
        return self


class ListSmsSignsForAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSmsSignsForAccountResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSmsSignsForAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCorsDomainsRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
    ):
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class ListCorsDomainsResponseBodyDomains(TeaModel):
    def __init__(
        self,
        domain: str = None,
        domain_id: str = None,
    ):
        self.domain = domain
        self.domain_id = domain_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        return self


class ListCorsDomainsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domains: List[ListCorsDomainsResponseBodyDomains] = None,
    ):
        self.request_id = request_id
        self.domains = domains

    def validate(self):
        if self.domains:
            for k in self.domains:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Domains'] = []
        if self.domains is not None:
            for k in self.domains:
                result['Domains'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.domains = []
        if m.get('Domains') is not None:
            for k in m.get('Domains'):
                temp_model = ListCorsDomainsResponseBodyDomains()
                self.domains.append(temp_model.from_map(k))
        return self


class ListCorsDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListCorsDomainsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListCorsDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDingtalkOpenPlatformConfigsRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
    ):
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class ListDingtalkOpenPlatformConfigsResponseBodyConfigs(TeaModel):
    def __init__(
        self,
        update_time: str = None,
        app_secret: str = None,
        app_id: str = None,
        create_time: str = None,
    ):
        self.update_time = update_time
        self.app_secret = app_secret
        self.app_id = app_id
        self.create_time = create_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        return self


class ListDingtalkOpenPlatformConfigsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        configs: List[ListDingtalkOpenPlatformConfigsResponseBodyConfigs] = None,
    ):
        self.request_id = request_id
        self.configs = configs

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['Configs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.configs = []
        if m.get('Configs') is not None:
            for k in m.get('Configs'):
                temp_model = ListDingtalkOpenPlatformConfigsResponseBodyConfigs()
                self.configs.append(temp_model.from_map(k))
        return self


class ListDingtalkOpenPlatformConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListDingtalkOpenPlatformConfigsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListDingtalkOpenPlatformConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDBExportTaskRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        collection: str = None,
        file_type: str = None,
        fields: str = None,
    ):
        self.space_id = space_id
        self.collection = collection
        self.file_type = file_type
        self.fields = fields

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.collection is not None:
            result['Collection'] = self.collection
        if self.file_type is not None:
            result['FileType'] = self.file_type
        if self.fields is not None:
            result['Fields'] = self.fields
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        if m.get('Fields') is not None:
            self.fields = m.get('Fields')
        return self


class CreateDBExportTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateDBExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateDBExportTaskResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateDBExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWebHostingConfigRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
    ):
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class GetWebHostingConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        allowed_ips: str = None,
        error_path: str = None,
        default_domain: str = None,
        index_path: str = None,
    ):
        self.space_id = space_id
        self.allowed_ips = allowed_ips
        self.error_path = error_path
        self.default_domain = default_domain
        self.index_path = index_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.allowed_ips is not None:
            result['AllowedIps'] = self.allowed_ips
        if self.error_path is not None:
            result['ErrorPath'] = self.error_path
        if self.default_domain is not None:
            result['DefaultDomain'] = self.default_domain
        if self.index_path is not None:
            result['IndexPath'] = self.index_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('AllowedIps') is not None:
            self.allowed_ips = m.get('AllowedIps')
        if m.get('ErrorPath') is not None:
            self.error_path = m.get('ErrorPath')
        if m.get('DefaultDomain') is not None:
            self.default_domain = m.get('DefaultDomain')
        if m.get('IndexPath') is not None:
            self.index_path = m.get('IndexPath')
        return self


class GetWebHostingConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: GetWebHostingConfigResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = GetWebHostingConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class GetWebHostingConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetWebHostingConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetWebHostingConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindWebHostingCustomDomainRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        custom_domain: str = None,
    ):
        self.space_id = space_id
        self.custom_domain = custom_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.custom_domain is not None:
            result['CustomDomain'] = self.custom_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('CustomDomain') is not None:
            self.custom_domain = m.get('CustomDomain')
        return self


class UnbindWebHostingCustomDomainResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnbindWebHostingCustomDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UnbindWebHostingCustomDomainResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnbindWebHostingCustomDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSmsTemplateRequest(TeaModel):
    def __init__(
        self,
        template_code: str = None,
        space_id: str = None,
    ):
        self.template_code = template_code
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DescribeSmsTemplateResponseBody(TeaModel):
    def __init__(
        self,
        update_time: str = None,
        template_content: str = None,
        request_id: str = None,
        create_time: str = None,
        template_type: str = None,
        template_name: str = None,
    ):
        self.update_time = update_time
        self.template_content = template_content
        self.request_id = request_id
        self.create_time = create_time
        self.template_type = template_type
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        return self


class DescribeSmsTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSmsTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSmsTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveWebHostingCustomDomainCorsConfigRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        domain_name: str = None,
        enable_cors: bool = None,
        access_control_allow_origin: str = None,
    ):
        self.space_id = space_id
        self.domain_name = domain_name
        self.enable_cors = enable_cors
        self.access_control_allow_origin = access_control_allow_origin

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name
        if self.enable_cors is not None:
            result['EnableCors'] = self.enable_cors
        if self.access_control_allow_origin is not None:
            result['AccessControlAllowOrigin'] = self.access_control_allow_origin
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')
        if m.get('EnableCors') is not None:
            self.enable_cors = m.get('EnableCors')
        if m.get('AccessControlAllowOrigin') is not None:
            self.access_control_allow_origin = m.get('AccessControlAllowOrigin')
        return self


class SaveWebHostingCustomDomainCorsConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        http_status_code: str = None,
        request_id: str = None,
        success: bool = None,
        data: bool = None,
    ):
        # Id of the request
        self.code = code
        self.message = message
        self.http_status_code = http_status_code
        self.request_id = request_id
        self.success = success
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class SaveWebHostingCustomDomainCorsConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SaveWebHostingCustomDomainCorsConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SaveWebHostingCustomDomainCorsConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BatchDeleteWebHostingFilesRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        file_paths: List[str] = None,
    ):
        self.space_id = space_id
        self.file_paths = file_paths

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.file_paths is not None:
            result['FilePaths'] = self.file_paths
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('FilePaths') is not None:
            self.file_paths = m.get('FilePaths')
        return self


class BatchDeleteWebHostingFilesResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BatchDeleteWebHostingFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: BatchDeleteWebHostingFilesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = BatchDeleteWebHostingFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCorsDomainRequest(TeaModel):
    def __init__(
        self,
        domain_id: str = None,
        space_id: str = None,
    ):
        self.domain_id = domain_id
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DeleteCorsDomainResponseBody(TeaModel):
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


class DeleteCorsDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteCorsDomainResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteCorsDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeHttpTriggerConfigRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
    ):
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DescribeHttpTriggerConfigResponseBody(TeaModel):
    def __init__(
        self,
        enable_service: bool = None,
        custom_domain_cname: str = None,
        request_id: str = None,
        default_endpoint: str = None,
        custom_domain_certificate_info: str = None,
        custom_domain: str = None,
    ):
        self.enable_service = enable_service
        self.custom_domain_cname = custom_domain_cname
        self.request_id = request_id
        self.default_endpoint = default_endpoint
        self.custom_domain_certificate_info = custom_domain_certificate_info
        self.custom_domain = custom_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_service is not None:
            result['EnableService'] = self.enable_service
        if self.custom_domain_cname is not None:
            result['CustomDomainCname'] = self.custom_domain_cname
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.default_endpoint is not None:
            result['DefaultEndpoint'] = self.default_endpoint
        if self.custom_domain_certificate_info is not None:
            result['CustomDomainCertificateInfo'] = self.custom_domain_certificate_info
        if self.custom_domain is not None:
            result['CustomDomain'] = self.custom_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableService') is not None:
            self.enable_service = m.get('EnableService')
        if m.get('CustomDomainCname') is not None:
            self.custom_domain_cname = m.get('CustomDomainCname')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DefaultEndpoint') is not None:
            self.default_endpoint = m.get('DefaultEndpoint')
        if m.get('CustomDomainCertificateInfo') is not None:
            self.custom_domain_certificate_info = m.get('CustomDomainCertificateInfo')
        if m.get('CustomDomain') is not None:
            self.custom_domain = m.get('CustomDomain')
        return self


class DescribeHttpTriggerConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeHttpTriggerConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeHttpTriggerConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveAppAuthTokenRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        isv_app_id: str = None,
        app_id: str = None,
        app_auth_token: str = None,
    ):
        self.space_id = space_id
        self.isv_app_id = isv_app_id
        self.app_id = app_id
        self.app_auth_token = app_auth_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.isv_app_id is not None:
            result['IsvAppId'] = self.isv_app_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_auth_token is not None:
            result['AppAuthToken'] = self.app_auth_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('IsvAppId') is not None:
            self.isv_app_id = m.get('IsvAppId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppAuthToken') is not None:
            self.app_auth_token = m.get('AppAuthToken')
        return self


class SaveAppAuthTokenResponseBody(TeaModel):
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


class SaveAppAuthTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SaveAppAuthTokenResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SaveAppAuthTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSmsSignStatusRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        sign_ids: str = None,
    ):
        self.space_id = space_id
        self.sign_ids = sign_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.sign_ids is not None:
            result['SignIds'] = self.sign_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('SignIds') is not None:
            self.sign_ids = m.get('SignIds')
        return self


class DescribeSmsSignStatusResponseBodySignStatuses(TeaModel):
    def __init__(
        self,
        sign_id: str = None,
        sign_status: int = None,
        reason: str = None,
        sign_name: str = None,
    ):
        self.sign_id = sign_id
        self.sign_status = sign_status
        self.reason = reason
        self.sign_name = sign_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sign_id is not None:
            result['SignId'] = self.sign_id
        if self.sign_status is not None:
            result['SignStatus'] = self.sign_status
        if self.reason is not None:
            result['Reason'] = self.reason
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SignId') is not None:
            self.sign_id = m.get('SignId')
        if m.get('SignStatus') is not None:
            self.sign_status = m.get('SignStatus')
        if m.get('Reason') is not None:
            self.reason = m.get('Reason')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        return self


class DescribeSmsSignStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        sign_statuses: List[DescribeSmsSignStatusResponseBodySignStatuses] = None,
    ):
        self.request_id = request_id
        self.sign_statuses = sign_statuses

    def validate(self):
        if self.sign_statuses:
            for k in self.sign_statuses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SignStatuses'] = []
        if self.sign_statuses is not None:
            for k in self.sign_statuses:
                result['SignStatuses'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sign_statuses = []
        if m.get('SignStatuses') is not None:
            for k in m.get('SignStatuses'):
                temp_model = DescribeSmsSignStatusResponseBodySignStatuses()
                self.sign_statuses.append(temp_model.from_map(k))
        return self


class DescribeSmsSignStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSmsSignStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSmsSignStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveWechatOpenPlatformConfigRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        app_id: str = None,
        app_secret: str = None,
    ):
        self.space_id = space_id
        self.app_id = app_id
        self.app_secret = app_secret

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_secret is not None:
            result['AppSecret'] = self.app_secret
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppSecret') is not None:
            self.app_secret = m.get('AppSecret')
        return self


class SaveWechatOpenPlatformConfigResponseBody(TeaModel):
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


class SaveWechatOpenPlatformConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SaveWechatOpenPlatformConfigResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = SaveWechatOpenPlatformConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeSpaceRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
    ):
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DescribeSpaceResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        space_id: str = None,
        request_id: str = None,
        gmt_create: str = None,
        name: str = None,
        desc: str = None,
    ):
        self.status = status
        self.space_id = space_id
        self.request_id = request_id
        self.gmt_create = gmt_create
        self.name = name
        self.desc = desc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.name is not None:
            result['Name'] = self.name
        if self.desc is not None:
            result['Desc'] = self.desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        return self


class DescribeSpaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeSpaceResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeSpaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RenameDBCollectionRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        origin_collection: str = None,
        new_collection: str = None,
    ):
        self.space_id = space_id
        self.origin_collection = origin_collection
        self.new_collection = new_collection

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.origin_collection is not None:
            result['OriginCollection'] = self.origin_collection
        if self.new_collection is not None:
            result['NewCollection'] = self.new_collection
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('OriginCollection') is not None:
            self.origin_collection = m.get('OriginCollection')
        if m.get('NewCollection') is not None:
            self.new_collection = m.get('NewCollection')
        return self


class RenameDBCollectionResponseBody(TeaModel):
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


class RenameDBCollectionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RenameDBCollectionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RenameDBCollectionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSmsSignsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        space_id: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class ListSmsSignsResponseBodySmsSigns(TeaModel):
    def __init__(
        self,
        update_time: str = None,
        sign_id: str = None,
        remark: str = None,
        sign_name: str = None,
        create_time: str = None,
    ):
        self.update_time = update_time
        self.sign_id = sign_id
        self.remark = remark
        self.sign_name = sign_name
        self.create_time = create_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.sign_id is not None:
            result['SignId'] = self.sign_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('SignId') is not None:
            self.sign_id = m.get('SignId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        return self


class ListSmsSignsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        sms_signs: List[ListSmsSignsResponseBodySmsSigns] = None,
    ):
        self.request_id = request_id
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count
        self.sms_signs = sms_signs

    def validate(self):
        if self.sms_signs:
            for k in self.sms_signs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['SmsSigns'] = []
        if self.sms_signs is not None:
            for k in self.sms_signs:
                result['SmsSigns'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.sms_signs = []
        if m.get('SmsSigns') is not None:
            for k in m.get('SmsSigns'):
                temp_model = ListSmsSignsResponseBodySmsSigns()
                self.sms_signs.append(temp_model.from_map(k))
        return self


class ListSmsSignsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSmsSignsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListSmsSignsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProductOpenStatusRequestLabels(TeaModel):
    def __init__(
        self,
        value: str = None,
        name: str = None,
    ):
        self.value = value
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class DescribeProductOpenStatusRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        desc: str = None,
        labels: List[DescribeProductOpenStatusRequestLabels] = None,
    ):
        self.name = name
        self.desc = desc
        self.labels = labels

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.desc is not None:
            result['Desc'] = self.desc
        result['Labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['Labels'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        self.labels = []
        if m.get('Labels') is not None:
            for k in m.get('Labels'):
                temp_model = DescribeProductOpenStatusRequestLabels()
                self.labels.append(temp_model.from_map(k))
        return self


class DescribeProductOpenStatusResponseBody(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        request_id: str = None,
    ):
        self.space_id = space_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeProductOpenStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeProductOpenStatusResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeProductOpenStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSmsSignRequest(TeaModel):
    def __init__(
        self,
        sign_id: str = None,
        remark: str = None,
        space_id: str = None,
        sign_name: str = None,
    ):
        self.sign_id = sign_id
        self.remark = remark
        self.space_id = space_id
        self.sign_name = sign_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sign_id is not None:
            result['SignId'] = self.sign_id
        if self.remark is not None:
            result['Remark'] = self.remark
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SignId') is not None:
            self.sign_id = m.get('SignId')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        return self


class UpdateSmsSignResponseBody(TeaModel):
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


class UpdateSmsSignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateSmsSignResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateSmsSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWebHostingCertificateRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        domain: str = None,
    ):
        self.space_id = space_id
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class DeleteWebHostingCertificateResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteWebHostingCertificateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteWebHostingCertificateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteWebHostingCertificateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDBBackupDumpTimesRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
    ):
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class QueryDBBackupDumpTimesResponseBodyBackupDumpTimes(TeaModel):
    def __init__(
        self,
        backup_id: str = None,
        dump_time: str = None,
    ):
        self.backup_id = backup_id
        self.dump_time = dump_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.backup_id is not None:
            result['BackupId'] = self.backup_id
        if self.dump_time is not None:
            result['DumpTime'] = self.dump_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupId') is not None:
            self.backup_id = m.get('BackupId')
        if m.get('DumpTime') is not None:
            self.dump_time = m.get('DumpTime')
        return self


class QueryDBBackupDumpTimesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        backup_dump_times: List[QueryDBBackupDumpTimesResponseBodyBackupDumpTimes] = None,
    ):
        self.request_id = request_id
        self.backup_dump_times = backup_dump_times

    def validate(self):
        if self.backup_dump_times:
            for k in self.backup_dump_times:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['BackupDumpTimes'] = []
        if self.backup_dump_times is not None:
            for k in self.backup_dump_times:
                result['BackupDumpTimes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.backup_dump_times = []
        if m.get('BackupDumpTimes') is not None:
            for k in m.get('BackupDumpTimes'):
                temp_model = QueryDBBackupDumpTimesResponseBodyBackupDumpTimes()
                self.backup_dump_times.append(temp_model.from_map(k))
        return self


class QueryDBBackupDumpTimesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: QueryDBBackupDumpTimesResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = QueryDBBackupDumpTimesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeployFunctionRequest(TeaModel):
    def __init__(
        self,
        deployment_id: str = None,
        space_id: str = None,
    ):
        self.deployment_id = deployment_id
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deployment_id is not None:
            result['DeploymentId'] = self.deployment_id
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeploymentId') is not None:
            self.deployment_id = m.get('DeploymentId')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DeployFunctionResponseBody(TeaModel):
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


class DeployFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeployFunctionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeployFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachSmsSignRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        sign_name: str = None,
    ):
        self.space_id = space_id
        self.sign_name = sign_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.sign_name is not None:
            result['SignName'] = self.sign_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('SignName') is not None:
            self.sign_name = m.get('SignName')
        return self


class AttachSmsSignResponseBody(TeaModel):
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


class AttachSmsSignResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AttachSmsSignResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AttachSmsSignResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateServicePolicyRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        service_name: str = None,
        policy: str = None,
        collection_name: str = None,
        policy_name: str = None,
    ):
        self.space_id = space_id
        self.service_name = service_name
        self.policy = policy
        self.collection_name = collection_name
        self.policy_name = policy_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.collection_name is not None:
            result['CollectionName'] = self.collection_name
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('CollectionName') is not None:
            self.collection_name = m.get('CollectionName')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        return self


class UpdateServicePolicyResponseBody(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        request_id: str = None,
        policy: str = None,
        policy_name: str = None,
        service_name: str = None,
        collection_name: str = None,
    ):
        self.space_id = space_id
        self.request_id = request_id
        self.policy = policy
        self.policy_name = policy_name
        self.service_name = service_name
        self.collection_name = collection_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.policy_name is not None:
            result['PolicyName'] = self.policy_name
        if self.service_name is not None:
            result['ServiceName'] = self.service_name
        if self.collection_name is not None:
            result['CollectionName'] = self.collection_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('PolicyName') is not None:
            self.policy_name = m.get('PolicyName')
        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')
        if m.get('CollectionName') is not None:
            self.collection_name = m.get('CollectionName')
        return self


class UpdateServicePolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateServicePolicyResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateServicePolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddCorsDomainRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        space_id: str = None,
    ):
        self.domain = domain
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class AddCorsDomainResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        domain_id: str = None,
    ):
        self.request_id = request_id
        self.domain_id = domain_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.domain_id is not None:
            result['DomainId'] = self.domain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')
        return self


class AddCorsDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddCorsDomainResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddCorsDomainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWebHostingFileRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        file_path: str = None,
    ):
        self.space_id = space_id
        self.file_path = file_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        return self


class DescribeWebHostingFileResponseBodyData(TeaModel):
    def __init__(
        self,
        file_path: str = None,
        content_type: str = None,
        etag: str = None,
        size: int = None,
        exists: bool = None,
        last_modified_time: int = None,
        signed_url: str = None,
    ):
        self.file_path = file_path
        self.content_type = content_type
        self.etag = etag
        self.size = size
        self.exists = exists
        self.last_modified_time = last_modified_time
        self.signed_url = signed_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.etag is not None:
            result['ETag'] = self.etag
        if self.size is not None:
            result['Size'] = self.size
        if self.exists is not None:
            result['Exists'] = self.exists
        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time
        if self.signed_url is not None:
            result['SignedUrl'] = self.signed_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('ETag') is not None:
            self.etag = m.get('ETag')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Exists') is not None:
            self.exists = m.get('Exists')
        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')
        if m.get('SignedUrl') is not None:
            self.signed_url = m.get('SignedUrl')
        return self


class DescribeWebHostingFileResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: DescribeWebHostingFileResponseBodyData = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            temp_model = DescribeWebHostingFileResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        return self


class DescribeWebHostingFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DescribeWebHostingFileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeWebHostingFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSmsTemplateRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        template_code: str = None,
        template_type: str = None,
        template_name: str = None,
        template_content: str = None,
        remark: str = None,
    ):
        self.space_id = space_id
        self.template_code = template_code
        self.template_type = template_type
        self.template_name = template_name
        self.template_content = template_content
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.template_code is not None:
            result['TemplateCode'] = self.template_code
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_content is not None:
            result['TemplateContent'] = self.template_content
        if self.remark is not None:
            result['Remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('TemplateCode') is not None:
            self.template_code = m.get('TemplateCode')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')
        if m.get('Remark') is not None:
            self.remark = m.get('Remark')
        return self


class UpdateSmsTemplateResponseBody(TeaModel):
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


class UpdateSmsTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateSmsTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpdateSmsTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyBuiltinFunctionTemplateRequest(TeaModel):
    def __init__(
        self,
        builtin_function_template_id: str = None,
        status: str = None,
    ):
        self.builtin_function_template_id = builtin_function_template_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.builtin_function_template_id is not None:
            result['BuiltinFunctionTemplateId'] = self.builtin_function_template_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuiltinFunctionTemplateId') is not None:
            self.builtin_function_template_id = m.get('BuiltinFunctionTemplateId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class VerifyBuiltinFunctionTemplateResponseBody(TeaModel):
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


class VerifyBuiltinFunctionTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: VerifyBuiltinFunctionTemplateResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = VerifyBuiltinFunctionTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWebHostingFileRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        file_path: str = None,
    ):
        self.space_id = space_id
        self.file_path = file_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        return self


class DeleteWebHostingFileResponseBody(TeaModel):
    def __init__(
        self,
        data: bool = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteWebHostingFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteWebHostingFileResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteWebHostingFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWebHostingCustomDomainsRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
    ):
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class ListWebHostingCustomDomainsResponseBodyData(TeaModel):
    def __init__(
        self,
        status: str = None,
        domain: str = None,
        update_time: int = None,
        ssl_protocol: str = None,
        force_redirect_type: str = None,
        description: str = None,
        create_time: int = None,
        cname: str = None,
        enable_cors: bool = None,
        access_control_allow_origin: str = None,
    ):
        self.status = status
        self.domain = domain
        self.update_time = update_time
        self.ssl_protocol = ssl_protocol
        self.force_redirect_type = force_redirect_type
        self.description = description
        self.create_time = create_time
        self.cname = cname
        self.enable_cors = enable_cors
        self.access_control_allow_origin = access_control_allow_origin

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.ssl_protocol is not None:
            result['SslProtocol'] = self.ssl_protocol
        if self.force_redirect_type is not None:
            result['ForceRedirectType'] = self.force_redirect_type
        if self.description is not None:
            result['Description'] = self.description
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.enable_cors is not None:
            result['EnableCors'] = self.enable_cors
        if self.access_control_allow_origin is not None:
            result['AccessControlAllowOrigin'] = self.access_control_allow_origin
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('SslProtocol') is not None:
            self.ssl_protocol = m.get('SslProtocol')
        if m.get('ForceRedirectType') is not None:
            self.force_redirect_type = m.get('ForceRedirectType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('EnableCors') is not None:
            self.enable_cors = m.get('EnableCors')
        if m.get('AccessControlAllowOrigin') is not None:
            self.access_control_allow_origin = m.get('AccessControlAllowOrigin')
        return self


class ListWebHostingCustomDomainsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        data: List[ListWebHostingCustomDomainsResponseBodyData] = None,
    ):
        self.request_id = request_id
        self.data = data

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListWebHostingCustomDomainsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        return self


class ListWebHostingCustomDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListWebHostingCustomDomainsResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListWebHostingCustomDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunDBCommandRequest(TeaModel):
    def __init__(
        self,
        space_id: str = None,
        body: str = None,
    ):
        self.space_id = space_id
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        if self.body is not None:
            result['Body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        return self


class RunDBCommandResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: str = None,
        affected_docs: int = None,
    ):
        self.request_id = request_id
        self.result = result
        self.affected_docs = affected_docs

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.affected_docs is not None:
            result['AffectedDocs'] = self.affected_docs
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('AffectedDocs') is not None:
            self.affected_docs = m.get('AffectedDocs')
        return self


class RunDBCommandResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RunDBCommandResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RunDBCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFunctionRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        space_id: str = None,
    ):
        self.name = name
        self.space_id = space_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.space_id is not None:
            result['SpaceId'] = self.space_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')
        return self


class DeleteFunctionResponseBody(TeaModel):
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


class DeleteFunctionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteFunctionResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteFunctionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


