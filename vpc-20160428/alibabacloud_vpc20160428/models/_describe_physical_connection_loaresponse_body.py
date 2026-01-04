# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribePhysicalConnectionLOAResponseBody(DaraModel):
    def __init__(
        self,
        physical_connection_loatype: main_models.DescribePhysicalConnectionLOAResponseBodyPhysicalConnectionLOAType = None,
        request_id: str = None,
    ):
        # The LOA information about the Express Connect circuit.
        self.physical_connection_loatype = physical_connection_loatype
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.physical_connection_loatype:
            self.physical_connection_loatype.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.physical_connection_loatype is not None:
            result['PhysicalConnectionLOAType'] = self.physical_connection_loatype.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhysicalConnectionLOAType') is not None:
            temp_model = main_models.DescribePhysicalConnectionLOAResponseBodyPhysicalConnectionLOAType()
            self.physical_connection_loatype = temp_model.from_map(m.get('PhysicalConnectionLOAType'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePhysicalConnectionLOAResponseBodyPhysicalConnectionLOAType(DaraModel):
    def __init__(
        self,
        company_localized_name: str = None,
        company_name: str = None,
        construction_time: str = None,
        instance_id: str = None,
        line_code: str = None,
        line_label: str = None,
        line_spcontact_info: str = None,
        line_service_provider: str = None,
        line_type: str = None,
        loa_url: str = None,
        pminfo: main_models.DescribePhysicalConnectionLOAResponseBodyPhysicalConnectionLOATypePMInfo = None,
        si: str = None,
        status: str = None,
    ):
        # The name of the construction company.
        self.company_localized_name = company_localized_name
        # The name of the organization that requires the Express Connect circuit.
        self.company_name = company_name
        # The time when construction starts.
        self.construction_time = construction_time
        # The ID of the Express Connect circuit.
        self.instance_id = instance_id
        # The circuit code provided by the connectivity provider.
        self.line_code = line_code
        # The label of the cable in the data center.
        self.line_label = line_label
        # The contact information about line O\\&M.
        self.line_spcontact_info = line_spcontact_info
        # The ISP. Valid values:
        # 
        # *   **China Telecom**
        # *   **China Unicom**
        # *   **China Mobile**
        # *   **Other ISPs in China**
        self.line_service_provider = line_service_provider
        # The type of the Express Connect circuit. Valid values:
        # 
        # *   **MSTP**
        # *   **MPLSVPN**
        # *   **FIBRE**
        # *   **Other**
        self.line_type = line_type
        # The download URL of the LOA file.
        self.loa_url = loa_url
        # The information about the construction workers.
        self.pminfo = pminfo
        # The on-site construction company.
        self.si = si
        # The status of the LOA. Valid values:
        # 
        # *   **Applying**: The LOA is pending for approval.
        # *   **Accept**: The LOA is approved.
        # *   **Available**: The LOA is available.
        # *   **Rejected**: The LOA is rejected.
        # *   **Completing**: The Express Connect circuit is under construction.
        # *   **Complete**: The Express Connect circuit is installed.
        # *   **Deleted**: The LOA is deleted.
        self.status = status

    def validate(self):
        if self.pminfo:
            self.pminfo.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.company_localized_name is not None:
            result['CompanyLocalizedName'] = self.company_localized_name

        if self.company_name is not None:
            result['CompanyName'] = self.company_name

        if self.construction_time is not None:
            result['ConstructionTime'] = self.construction_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.line_code is not None:
            result['LineCode'] = self.line_code

        if self.line_label is not None:
            result['LineLabel'] = self.line_label

        if self.line_spcontact_info is not None:
            result['LineSPContactInfo'] = self.line_spcontact_info

        if self.line_service_provider is not None:
            result['LineServiceProvider'] = self.line_service_provider

        if self.line_type is not None:
            result['LineType'] = self.line_type

        if self.loa_url is not None:
            result['LoaUrl'] = self.loa_url

        if self.pminfo is not None:
            result['PMInfo'] = self.pminfo.to_map()

        if self.si is not None:
            result['SI'] = self.si

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompanyLocalizedName') is not None:
            self.company_localized_name = m.get('CompanyLocalizedName')

        if m.get('CompanyName') is not None:
            self.company_name = m.get('CompanyName')

        if m.get('ConstructionTime') is not None:
            self.construction_time = m.get('ConstructionTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LineCode') is not None:
            self.line_code = m.get('LineCode')

        if m.get('LineLabel') is not None:
            self.line_label = m.get('LineLabel')

        if m.get('LineSPContactInfo') is not None:
            self.line_spcontact_info = m.get('LineSPContactInfo')

        if m.get('LineServiceProvider') is not None:
            self.line_service_provider = m.get('LineServiceProvider')

        if m.get('LineType') is not None:
            self.line_type = m.get('LineType')

        if m.get('LoaUrl') is not None:
            self.loa_url = m.get('LoaUrl')

        if m.get('PMInfo') is not None:
            temp_model = main_models.DescribePhysicalConnectionLOAResponseBodyPhysicalConnectionLOATypePMInfo()
            self.pminfo = temp_model.from_map(m.get('PMInfo'))

        if m.get('SI') is not None:
            self.si = m.get('SI')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribePhysicalConnectionLOAResponseBodyPhysicalConnectionLOATypePMInfo(DaraModel):
    def __init__(
        self,
        pminfo: List[main_models.DescribePhysicalConnectionLOAResponseBodyPhysicalConnectionLOATypePMInfoPMInfo] = None,
    ):
        self.pminfo = pminfo

    def validate(self):
        if self.pminfo:
            for v1 in self.pminfo:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['PMInfo'] = []
        if self.pminfo is not None:
            for k1 in self.pminfo:
                result['PMInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.pminfo = []
        if m.get('PMInfo') is not None:
            for k1 in m.get('PMInfo'):
                temp_model = main_models.DescribePhysicalConnectionLOAResponseBodyPhysicalConnectionLOATypePMInfoPMInfo()
                self.pminfo.append(temp_model.from_map(k1))

        return self

class DescribePhysicalConnectionLOAResponseBodyPhysicalConnectionLOATypePMInfoPMInfo(DaraModel):
    def __init__(
        self,
        pmcertificate_no: str = None,
        pmcertificate_type: str = None,
        pmcontact_info: str = None,
        pmgender: str = None,
        pmname: str = None,
    ):
        # The identity document number of the construction worker.
        self.pmcertificate_no = pmcertificate_no
        # The identity document type of the construction worker. Valid values:
        # 
        # *   **IDCard**
        # *   **Passport**
        # *   **Other**
        self.pmcertificate_type = pmcertificate_type
        # The phone number of the construction worker.
        self.pmcontact_info = pmcontact_info
        # The gender of the construction worker. Valid values:
        # 
        # *   **Male**
        # *   **Female**
        self.pmgender = pmgender
        # The name of the construction worker.
        self.pmname = pmname

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.pmcertificate_no is not None:
            result['PMCertificateNo'] = self.pmcertificate_no

        if self.pmcertificate_type is not None:
            result['PMCertificateType'] = self.pmcertificate_type

        if self.pmcontact_info is not None:
            result['PMContactInfo'] = self.pmcontact_info

        if self.pmgender is not None:
            result['PMGender'] = self.pmgender

        if self.pmname is not None:
            result['PMName'] = self.pmname

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PMCertificateNo') is not None:
            self.pmcertificate_no = m.get('PMCertificateNo')

        if m.get('PMCertificateType') is not None:
            self.pmcertificate_type = m.get('PMCertificateType')

        if m.get('PMContactInfo') is not None:
            self.pmcontact_info = m.get('PMContactInfo')

        if m.get('PMGender') is not None:
            self.pmgender = m.get('PMGender')

        if m.get('PMName') is not None:
            self.pmname = m.get('PMName')

        return self

