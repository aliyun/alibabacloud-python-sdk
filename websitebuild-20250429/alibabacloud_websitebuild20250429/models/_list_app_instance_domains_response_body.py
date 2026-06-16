# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_websitebuild20250429 import models as main_models
from darabonba.model import DaraModel

class ListAppInstanceDomainsResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        allow_retry: bool = None,
        app_name: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        error_args: List[Any] = None,
        max_results: int = None,
        module: main_models.ListAppInstanceDomainsResponseBodyModule = None,
        next_token: str = None,
        request_id: str = None,
        root_error_code: str = None,
        root_error_msg: str = None,
        synchro: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # Indicates whether a retry is allowed.
        self.allow_retry = allow_retry
        # The application name.
        self.app_name = app_name
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message, which is used to replace the `%s` placeholder in the **ErrMessage** response parameter.
        # > If **ErrMessage** returns **The Value of Input Parameter %s is not valid** and **DynamicMessage** returns **DtsJobId**, the value of the **DtsJobId** request parameter is invalid.
        self.dynamic_message = dynamic_message
        # The error parameters.
        self.error_args = error_args
        # The maximum number of entries to return per query.
        # 
        # Valid values: 10 to 100. Default value: 20.
        self.max_results = max_results
        # The response data.
        self.module = module
        # The token for the next query. This parameter is empty if there are no more results.
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        # The error code.
        self.root_error_code = root_error_code
        # The error message.
        self.root_error_msg = root_error_msg
        # A reserved parameter.
        self.synchro = synchro

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.allow_retry is not None:
            result['AllowRetry'] = self.allow_retry

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.error_args is not None:
            result['ErrorArgs'] = self.error_args

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.module is not None:
            result['Module'] = self.module.to_map()

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.root_error_code is not None:
            result['RootErrorCode'] = self.root_error_code

        if self.root_error_msg is not None:
            result['RootErrorMsg'] = self.root_error_msg

        if self.synchro is not None:
            result['Synchro'] = self.synchro

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('AllowRetry') is not None:
            self.allow_retry = m.get('AllowRetry')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrorArgs') is not None:
            self.error_args = m.get('ErrorArgs')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Module') is not None:
            temp_model = main_models.ListAppInstanceDomainsResponseBodyModule()
            self.module = temp_model.from_map(m.get('Module'))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RootErrorCode') is not None:
            self.root_error_code = m.get('RootErrorCode')

        if m.get('RootErrorMsg') is not None:
            self.root_error_msg = m.get('RootErrorMsg')

        if m.get('Synchro') is not None:
            self.synchro = m.get('Synchro')

        return self

class ListAppInstanceDomainsResponseBodyModule(DaraModel):
    def __init__(
        self,
        current_page_num: int = None,
        data: List[main_models.ListAppInstanceDomainsResponseBodyModuleData] = None,
        next: main_models.ListAppInstanceDomainsResponseBodyModuleNext = None,
        next_page: bool = None,
        page_size: int = None,
        pre_page: bool = None,
        result_limit: bool = None,
        total_item_num: int = None,
        total_page_num: int = None,
    ):
        # The current page number.
        self.current_page_num = current_page_num
        # The query results.
        self.data = data
        # The decision weight.
        self.next = next
        # Indicates whether a next page exists.
        self.next_page = next_page
        # The page size.
        self.page_size = page_size
        # Indicates whether a previous page exists.
        self.pre_page = pre_page
        # In addition to pagination limits, the server processes up to 1,000 recent records per query. If the results exceed 1,000 records, **ResultLimit** is **true**. In this case, narrow the time range and search again. Otherwise, **ResultLimit** is **false**.
        self.result_limit = result_limit
        # The total number of entries.
        self.total_item_num = total_item_num
        # The total number of pages.
        self.total_page_num = total_page_num

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()
        if self.next:
            self.next.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.next is not None:
            result['Next'] = self.next.to_map()

        if self.next_page is not None:
            result['NextPage'] = self.next_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.pre_page is not None:
            result['PrePage'] = self.pre_page

        if self.result_limit is not None:
            result['ResultLimit'] = self.result_limit

        if self.total_item_num is not None:
            result['TotalItemNum'] = self.total_item_num

        if self.total_page_num is not None:
            result['TotalPageNum'] = self.total_page_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListAppInstanceDomainsResponseBodyModuleData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Next') is not None:
            temp_model = main_models.ListAppInstanceDomainsResponseBodyModuleNext()
            self.next = temp_model.from_map(m.get('Next'))

        if m.get('NextPage') is not None:
            self.next_page = m.get('NextPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PrePage') is not None:
            self.pre_page = m.get('PrePage')

        if m.get('ResultLimit') is not None:
            self.result_limit = m.get('ResultLimit')

        if m.get('TotalItemNum') is not None:
            self.total_item_num = m.get('TotalItemNum')

        if m.get('TotalPageNum') is not None:
            self.total_page_num = m.get('TotalPageNum')

        return self

class ListAppInstanceDomainsResponseBodyModuleNext(DaraModel):
    def __init__(
        self,
        certificate: main_models.ListAppInstanceDomainsResponseBodyModuleNextCertificate = None,
        create_time: str = None,
        domain_name: str = None,
        overall_status: str = None,
        ownership: main_models.ListAppInstanceDomainsResponseBodyModuleNextOwnership = None,
        qualification: main_models.ListAppInstanceDomainsResponseBodyModuleNextQualification = None,
        resolution: main_models.ListAppInstanceDomainsResponseBodyModuleNextResolution = None,
        verification: main_models.ListAppInstanceDomainsResponseBodyModuleNextVerification = None,
    ):
        # The SSL certificate information of the domain name.
        self.certificate = certificate
        # The time when the instance was created. Format: yyyy-MM-dd HH:mm:ss.
        self.create_time = create_time
        # The domain name.
        self.domain_name = domain_name
        # The overall binding status.
        self.overall_status = overall_status
        # The domain name ownership information.
        self.ownership = ownership
        # The domain name qualification information.
        self.qualification = qualification
        # The domain name resolution information.
        self.resolution = resolution
        # The domain name verification information.
        self.verification = verification

    def validate(self):
        if self.certificate:
            self.certificate.validate()
        if self.ownership:
            self.ownership.validate()
        if self.qualification:
            self.qualification.validate()
        if self.resolution:
            self.resolution.validate()
        if self.verification:
            self.verification.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate is not None:
            result['Certificate'] = self.certificate.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.overall_status is not None:
            result['OverallStatus'] = self.overall_status

        if self.ownership is not None:
            result['Ownership'] = self.ownership.to_map()

        if self.qualification is not None:
            result['Qualification'] = self.qualification.to_map()

        if self.resolution is not None:
            result['Resolution'] = self.resolution.to_map()

        if self.verification is not None:
            result['Verification'] = self.verification.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Certificate') is not None:
            temp_model = main_models.ListAppInstanceDomainsResponseBodyModuleNextCertificate()
            self.certificate = temp_model.from_map(m.get('Certificate'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('OverallStatus') is not None:
            self.overall_status = m.get('OverallStatus')

        if m.get('Ownership') is not None:
            temp_model = main_models.ListAppInstanceDomainsResponseBodyModuleNextOwnership()
            self.ownership = temp_model.from_map(m.get('Ownership'))

        if m.get('Qualification') is not None:
            temp_model = main_models.ListAppInstanceDomainsResponseBodyModuleNextQualification()
            self.qualification = temp_model.from_map(m.get('Qualification'))

        if m.get('Resolution') is not None:
            temp_model = main_models.ListAppInstanceDomainsResponseBodyModuleNextResolution()
            self.resolution = temp_model.from_map(m.get('Resolution'))

        if m.get('Verification') is not None:
            temp_model = main_models.ListAppInstanceDomainsResponseBodyModuleNextVerification()
            self.verification = temp_model.from_map(m.get('Verification'))

        return self

class ListAppInstanceDomainsResponseBodyModuleNextVerification(DaraModel):
    def __init__(
        self,
        dns_record: main_models.ListAppInstanceDomainsResponseBodyModuleNextVerificationDnsRecord = None,
        error_msg: str = None,
        verification_status: str = None,
    ):
        # The DNS record that the user needs to configure.
        self.dns_record = dns_record
        # The error message.
        self.error_msg = error_msg
        # The ownership verification status.
        self.verification_status = verification_status

    def validate(self):
        if self.dns_record:
            self.dns_record.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dns_record is not None:
            result['DnsRecord'] = self.dns_record.to_map()

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsRecord') is not None:
            temp_model = main_models.ListAppInstanceDomainsResponseBodyModuleNextVerificationDnsRecord()
            self.dns_record = temp_model.from_map(m.get('DnsRecord'))

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')

        return self

class ListAppInstanceDomainsResponseBodyModuleNextVerificationDnsRecord(DaraModel):
    def __init__(
        self,
        host: str = None,
        record_type: str = None,
        value: str = None,
    ):
        # The host record.
        self.host = host
        # The record type.
        self.record_type = record_type
        # The record value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host is not None:
            result['Host'] = self.host

        if self.record_type is not None:
            result['RecordType'] = self.record_type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListAppInstanceDomainsResponseBodyModuleNextResolution(DaraModel):
    def __init__(
        self,
        dns_record: main_models.ListAppInstanceDomainsResponseBodyModuleNextResolutionDnsRecord = None,
        error_msg: str = None,
        resolution_status: str = None,
    ):
        # The DNS record information.
        self.dns_record = dns_record
        # The error message.
        self.error_msg = error_msg
        # The domain name resolution status.
        self.resolution_status = resolution_status

    def validate(self):
        if self.dns_record:
            self.dns_record.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dns_record is not None:
            result['DnsRecord'] = self.dns_record.to_map()

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.resolution_status is not None:
            result['ResolutionStatus'] = self.resolution_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsRecord') is not None:
            temp_model = main_models.ListAppInstanceDomainsResponseBodyModuleNextResolutionDnsRecord()
            self.dns_record = temp_model.from_map(m.get('DnsRecord'))

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('ResolutionStatus') is not None:
            self.resolution_status = m.get('ResolutionStatus')

        return self

class ListAppInstanceDomainsResponseBodyModuleNextResolutionDnsRecord(DaraModel):
    def __init__(
        self,
        host: str = None,
        record_type: str = None,
        value: str = None,
    ):
        # The host record.
        self.host = host
        # The record type.
        self.record_type = record_type
        # The record value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host is not None:
            result['Host'] = self.host

        if self.record_type is not None:
            result['RecordType'] = self.record_type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListAppInstanceDomainsResponseBodyModuleNextQualification(DaraModel):
    def __init__(
        self,
        icp_record_number: str = None,
        icp_site_record_number: str = None,
        police_record_number: str = None,
    ):
        # The ICP entity filing number.
        self.icp_record_number = icp_record_number
        # The ICP website filing number.
        self.icp_site_record_number = icp_site_record_number
        # The public security filing number.
        self.police_record_number = police_record_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.icp_record_number is not None:
            result['IcpRecordNumber'] = self.icp_record_number

        if self.icp_site_record_number is not None:
            result['IcpSiteRecordNumber'] = self.icp_site_record_number

        if self.police_record_number is not None:
            result['PoliceRecordNumber'] = self.police_record_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IcpRecordNumber') is not None:
            self.icp_record_number = m.get('IcpRecordNumber')

        if m.get('IcpSiteRecordNumber') is not None:
            self.icp_site_record_number = m.get('IcpSiteRecordNumber')

        if m.get('PoliceRecordNumber') is not None:
            self.police_record_number = m.get('PoliceRecordNumber')

        return self

class ListAppInstanceDomainsResponseBodyModuleNextOwnership(DaraModel):
    def __init__(
        self,
        account: str = None,
        provider: str = None,
    ):
        # The account owner type. Valid values: CURRENT and OTHER.
        self.account = account
        # The registrar type. Valid values: ALIYUN and OTHER.
        self.provider = provider

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account

        if self.provider is not None:
            result['Provider'] = self.provider

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')

        if m.get('Provider') is not None:
            self.provider = m.get('Provider')

        return self

class ListAppInstanceDomainsResponseBodyModuleNextCertificate(DaraModel):
    def __init__(
        self,
        certificate_name: str = None,
        certificate_status: str = None,
        certificate_type: str = None,
        end_time: str = None,
    ):
        # The certificate name.
        self.certificate_name = certificate_name
        # The certificate status.
        self.certificate_status = certificate_status
        # The certificate type.
        self.certificate_type = certificate_type
        # The expiration date of the certificate.
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name

        if self.certificate_status is not None:
            result['CertificateStatus'] = self.certificate_status

        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')

        if m.get('CertificateStatus') is not None:
            self.certificate_status = m.get('CertificateStatus')

        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        return self

class ListAppInstanceDomainsResponseBodyModuleData(DaraModel):
    def __init__(
        self,
        certificate: main_models.ListAppInstanceDomainsResponseBodyModuleDataCertificate = None,
        create_time: str = None,
        domain_name: str = None,
        overall_status: str = None,
        ownership: main_models.ListAppInstanceDomainsResponseBodyModuleDataOwnership = None,
        qualification: main_models.ListAppInstanceDomainsResponseBodyModuleDataQualification = None,
        resolution: main_models.ListAppInstanceDomainsResponseBodyModuleDataResolution = None,
        verification: main_models.ListAppInstanceDomainsResponseBodyModuleDataVerification = None,
    ):
        # The SSL certificate information of the domain name.
        self.certificate = certificate
        # The time when the instance was created. Format: yyyy-MM-dd HH:mm:ss.
        self.create_time = create_time
        # The domain name.
        self.domain_name = domain_name
        # The overall binding status.
        self.overall_status = overall_status
        # The domain name ownership information.
        self.ownership = ownership
        # The domain name qualification information.
        self.qualification = qualification
        # The domain name resolution information.
        self.resolution = resolution
        # The domain name verification information.
        self.verification = verification

    def validate(self):
        if self.certificate:
            self.certificate.validate()
        if self.ownership:
            self.ownership.validate()
        if self.qualification:
            self.qualification.validate()
        if self.resolution:
            self.resolution.validate()
        if self.verification:
            self.verification.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate is not None:
            result['Certificate'] = self.certificate.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.overall_status is not None:
            result['OverallStatus'] = self.overall_status

        if self.ownership is not None:
            result['Ownership'] = self.ownership.to_map()

        if self.qualification is not None:
            result['Qualification'] = self.qualification.to_map()

        if self.resolution is not None:
            result['Resolution'] = self.resolution.to_map()

        if self.verification is not None:
            result['Verification'] = self.verification.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Certificate') is not None:
            temp_model = main_models.ListAppInstanceDomainsResponseBodyModuleDataCertificate()
            self.certificate = temp_model.from_map(m.get('Certificate'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('OverallStatus') is not None:
            self.overall_status = m.get('OverallStatus')

        if m.get('Ownership') is not None:
            temp_model = main_models.ListAppInstanceDomainsResponseBodyModuleDataOwnership()
            self.ownership = temp_model.from_map(m.get('Ownership'))

        if m.get('Qualification') is not None:
            temp_model = main_models.ListAppInstanceDomainsResponseBodyModuleDataQualification()
            self.qualification = temp_model.from_map(m.get('Qualification'))

        if m.get('Resolution') is not None:
            temp_model = main_models.ListAppInstanceDomainsResponseBodyModuleDataResolution()
            self.resolution = temp_model.from_map(m.get('Resolution'))

        if m.get('Verification') is not None:
            temp_model = main_models.ListAppInstanceDomainsResponseBodyModuleDataVerification()
            self.verification = temp_model.from_map(m.get('Verification'))

        return self

class ListAppInstanceDomainsResponseBodyModuleDataVerification(DaraModel):
    def __init__(
        self,
        dns_record: main_models.ListAppInstanceDomainsResponseBodyModuleDataVerificationDnsRecord = None,
        error_msg: str = None,
        verification_status: str = None,
        verification_status_code: str = None,
    ):
        # The DNS record that the user needs to configure.
        self.dns_record = dns_record
        # The error message.
        self.error_msg = error_msg
        # The ownership verification status.
        self.verification_status = verification_status
        # The ownership verification status code.
        self.verification_status_code = verification_status_code

    def validate(self):
        if self.dns_record:
            self.dns_record.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dns_record is not None:
            result['DnsRecord'] = self.dns_record.to_map()

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.verification_status is not None:
            result['VerificationStatus'] = self.verification_status

        if self.verification_status_code is not None:
            result['VerificationStatusCode'] = self.verification_status_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsRecord') is not None:
            temp_model = main_models.ListAppInstanceDomainsResponseBodyModuleDataVerificationDnsRecord()
            self.dns_record = temp_model.from_map(m.get('DnsRecord'))

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('VerificationStatus') is not None:
            self.verification_status = m.get('VerificationStatus')

        if m.get('VerificationStatusCode') is not None:
            self.verification_status_code = m.get('VerificationStatusCode')

        return self

class ListAppInstanceDomainsResponseBodyModuleDataVerificationDnsRecord(DaraModel):
    def __init__(
        self,
        host: str = None,
        record_type: str = None,
        value: str = None,
    ):
        # The host record.
        self.host = host
        # The record type.
        self.record_type = record_type
        # The record value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host is not None:
            result['Host'] = self.host

        if self.record_type is not None:
            result['RecordType'] = self.record_type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListAppInstanceDomainsResponseBodyModuleDataResolution(DaraModel):
    def __init__(
        self,
        dns_record: main_models.ListAppInstanceDomainsResponseBodyModuleDataResolutionDnsRecord = None,
        error_msg: str = None,
        resolution_status: str = None,
    ):
        # The DNS record information.
        self.dns_record = dns_record
        # The error message.
        self.error_msg = error_msg
        # The domain name resolution status.
        self.resolution_status = resolution_status

    def validate(self):
        if self.dns_record:
            self.dns_record.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dns_record is not None:
            result['DnsRecord'] = self.dns_record.to_map()

        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg

        if self.resolution_status is not None:
            result['ResolutionStatus'] = self.resolution_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DnsRecord') is not None:
            temp_model = main_models.ListAppInstanceDomainsResponseBodyModuleDataResolutionDnsRecord()
            self.dns_record = temp_model.from_map(m.get('DnsRecord'))

        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')

        if m.get('ResolutionStatus') is not None:
            self.resolution_status = m.get('ResolutionStatus')

        return self

class ListAppInstanceDomainsResponseBodyModuleDataResolutionDnsRecord(DaraModel):
    def __init__(
        self,
        host: str = None,
        record_type: str = None,
        value: str = None,
    ):
        # The host record.
        self.host = host
        # The record type.
        self.record_type = record_type
        # The record value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host is not None:
            result['Host'] = self.host

        if self.record_type is not None:
            result['RecordType'] = self.record_type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('RecordType') is not None:
            self.record_type = m.get('RecordType')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListAppInstanceDomainsResponseBodyModuleDataQualification(DaraModel):
    def __init__(
        self,
        icp_record_number: str = None,
        icp_site_record_number: str = None,
        police_record_number: str = None,
    ):
        # The ICP entity filing number.
        self.icp_record_number = icp_record_number
        # The ICP website filing number.
        self.icp_site_record_number = icp_site_record_number
        # The public security filing number.
        self.police_record_number = police_record_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.icp_record_number is not None:
            result['IcpRecordNumber'] = self.icp_record_number

        if self.icp_site_record_number is not None:
            result['IcpSiteRecordNumber'] = self.icp_site_record_number

        if self.police_record_number is not None:
            result['PoliceRecordNumber'] = self.police_record_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IcpRecordNumber') is not None:
            self.icp_record_number = m.get('IcpRecordNumber')

        if m.get('IcpSiteRecordNumber') is not None:
            self.icp_site_record_number = m.get('IcpSiteRecordNumber')

        if m.get('PoliceRecordNumber') is not None:
            self.police_record_number = m.get('PoliceRecordNumber')

        return self

class ListAppInstanceDomainsResponseBodyModuleDataOwnership(DaraModel):
    def __init__(
        self,
        account: str = None,
        provider: str = None,
        root_domain: str = None,
    ):
        # The account owner type. Valid values: CURRENT and OTHER.
        self.account = account
        # The registrar type. Valid values: ALIYUN and OTHER.
        self.provider = provider
        # The root domain name corresponding to the domain name.
        self.root_domain = root_domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account is not None:
            result['Account'] = self.account

        if self.provider is not None:
            result['Provider'] = self.provider

        if self.root_domain is not None:
            result['RootDomain'] = self.root_domain

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')

        if m.get('Provider') is not None:
            self.provider = m.get('Provider')

        if m.get('RootDomain') is not None:
            self.root_domain = m.get('RootDomain')

        return self

class ListAppInstanceDomainsResponseBodyModuleDataCertificate(DaraModel):
    def __init__(
        self,
        certificate_name: str = None,
        certificate_status: str = None,
        certificate_type: str = None,
        end_time: str = None,
    ):
        # The certificate name.
        self.certificate_name = certificate_name
        # The certificate status.
        self.certificate_status = certificate_status
        # The certificate type.
        self.certificate_type = certificate_type
        # The expiration date of the certificate.
        self.end_time = end_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate_name is not None:
            result['CertificateName'] = self.certificate_name

        if self.certificate_status is not None:
            result['CertificateStatus'] = self.certificate_status

        if self.certificate_type is not None:
            result['CertificateType'] = self.certificate_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CertificateName') is not None:
            self.certificate_name = m.get('CertificateName')

        if m.get('CertificateStatus') is not None:
            self.certificate_status = m.get('CertificateStatus')

        if m.get('CertificateType') is not None:
            self.certificate_type = m.get('CertificateType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        return self

