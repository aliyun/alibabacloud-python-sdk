# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeVulDetailsResponseBody(DaraModel):
    def __init__(
        self,
        cves: List[main_models.DescribeVulDetailsResponseBodyCves] = None,
        request_id: str = None,
    ):
        # The details of the vulnerability.
        self.cves = cves
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.cves:
            for v1 in self.cves:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Cves'] = []
        if self.cves is not None:
            for k1 in self.cves:
                result['Cves'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cves = []
        if m.get('Cves') is not None:
            for k1 in m.get('Cves'):
                temp_model = main_models.DescribeVulDetailsResponseBodyCves()
                self.cves.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeVulDetailsResponseBodyCves(DaraModel):
    def __init__(
        self,
        classify: str = None,
        classifys: List[main_models.DescribeVulDetailsResponseBodyCvesClassifys] = None,
        cnvd_id: str = None,
        complexity: str = None,
        content: str = None,
        cve_id: str = None,
        cve_link: str = None,
        cvss_score: str = None,
        cvss_vector: str = None,
        instance_name: str = None,
        internet_ip: str = None,
        intranet_ip: str = None,
        other_id: str = None,
        poc: str = None,
        poc_create_time: int = None,
        poc_disclosure_time: int = None,
        product: str = None,
        reference: str = None,
        release_time: int = None,
        solution: str = None,
        summary: str = None,
        target_id: str = None,
        target_name: str = None,
        title: str = None,
        vendor: str = None,
        vul_level: str = None,
    ):
        # The type of the vulnerability.
        self.classify = classify
        # The vulnerability types.
        self.classifys = classifys
        # The China National Vulnerability Database (CNVD) ID.
        self.cnvd_id = cnvd_id
        # The difficulty level of exploiting the vulnerability. Valid values:
        # 
        # *   **LOW**
        # *   **MEDIUM**
        # *   **HIGH**
        self.complexity = complexity
        # The CVE content.
        self.content = content
        # The Common Vulnerabilities and Exposures (CVE) ID.
        self.cve_id = cve_id
        # The link to the CVE details.
        self.cve_link = cve_link
        # The Common Vulnerability Scoring System (CVSS) score of the vulnerability in the Alibaba Cloud vulnerability library.
        self.cvss_score = cvss_score
        # The vector that is used to calculate the CVSS score.
        self.cvss_vector = cvss_vector
        # The name of the instance.
        # 
        # >  This parameter is deprecated. You can call the [DescribeVulList](~~DescribeVulList~~) operation to query the instance that is affected by the vulnerability.
        self.instance_name = instance_name
        # The public IP address of the server.
        # 
        # >  This parameter is deprecated. You can call the [DescribeVulList](~~DescribeVulList~~) operation to query the instance that is affected by the vulnerability.
        self.internet_ip = internet_ip
        # The private IP address of the server.
        # 
        # >  This parameter is deprecated. You can call the [DescribeVulList](~~DescribeVulList~~) operation to query the instance that is affected by the vulnerability.
        self.intranet_ip = intranet_ip
        # The ID of the vulnerability.
        self.other_id = other_id
        # The POC content.
        self.poc = poc
        # The UNIX timestamp when the proof of concept (POC) was created. Unit: milliseconds.
        self.poc_create_time = poc_create_time
        # The UNIX timestamp when the POC was disclosed. Unit: milliseconds.
        self.poc_disclosure_time = poc_disclosure_time
        # The service that is affected by the vulnerability.
        self.product = product
        # The reference of the vulnerability in the Alibaba Cloud vulnerability library. The value is a URL.
        self.reference = reference
        # The disclosure time that is displayed for the vulnerability in the Alibaba Cloud vulnerability library. The value is a UNIX timestamp. Unit: milliseconds.
        self.release_time = release_time
        # The fixing suggestions of the vulnerability.
        self.solution = solution
        # The introduction to the vulnerability.
        self.summary = summary
        # The ID of the asset that is scanned.
        # 
        # >  This parameter is deprecated. You can call the [DescribeVulList](~~DescribeVulList~~) operation to query the instance that is affected by the vulnerability.
        self.target_id = target_id
        # The name of the asset that is scanned.
        # 
        # >  This parameter is deprecated. You can call the [DescribeVulList](~~DescribeVulList~~) operation to query the instance that is affected by the vulnerability.
        self.target_name = target_name
        # The title of the vulnerability announcement.
        self.title = title
        # The vendor that disclosed the vulnerability.
        self.vendor = vendor
        # The severity of the vulnerability. Valid values:
        # 
        # *   **serious**
        # *   **high**
        # *   **medium**
        # *   **low**
        self.vul_level = vul_level

    def validate(self):
        if self.classifys:
            for v1 in self.classifys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.classify is not None:
            result['Classify'] = self.classify

        result['Classifys'] = []
        if self.classifys is not None:
            for k1 in self.classifys:
                result['Classifys'].append(k1.to_map() if k1 else None)

        if self.cnvd_id is not None:
            result['CnvdId'] = self.cnvd_id

        if self.complexity is not None:
            result['Complexity'] = self.complexity

        if self.content is not None:
            result['Content'] = self.content

        if self.cve_id is not None:
            result['CveId'] = self.cve_id

        if self.cve_link is not None:
            result['CveLink'] = self.cve_link

        if self.cvss_score is not None:
            result['CvssScore'] = self.cvss_score

        if self.cvss_vector is not None:
            result['CvssVector'] = self.cvss_vector

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_ip is not None:
            result['InternetIp'] = self.internet_ip

        if self.intranet_ip is not None:
            result['IntranetIp'] = self.intranet_ip

        if self.other_id is not None:
            result['OtherId'] = self.other_id

        if self.poc is not None:
            result['Poc'] = self.poc

        if self.poc_create_time is not None:
            result['PocCreateTime'] = self.poc_create_time

        if self.poc_disclosure_time is not None:
            result['PocDisclosureTime'] = self.poc_disclosure_time

        if self.product is not None:
            result['Product'] = self.product

        if self.reference is not None:
            result['Reference'] = self.reference

        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time

        if self.solution is not None:
            result['Solution'] = self.solution

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_name is not None:
            result['TargetName'] = self.target_name

        if self.title is not None:
            result['Title'] = self.title

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        if self.vul_level is not None:
            result['VulLevel'] = self.vul_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classify') is not None:
            self.classify = m.get('Classify')

        self.classifys = []
        if m.get('Classifys') is not None:
            for k1 in m.get('Classifys'):
                temp_model = main_models.DescribeVulDetailsResponseBodyCvesClassifys()
                self.classifys.append(temp_model.from_map(k1))

        if m.get('CnvdId') is not None:
            self.cnvd_id = m.get('CnvdId')

        if m.get('Complexity') is not None:
            self.complexity = m.get('Complexity')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('CveId') is not None:
            self.cve_id = m.get('CveId')

        if m.get('CveLink') is not None:
            self.cve_link = m.get('CveLink')

        if m.get('CvssScore') is not None:
            self.cvss_score = m.get('CvssScore')

        if m.get('CvssVector') is not None:
            self.cvss_vector = m.get('CvssVector')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetIp') is not None:
            self.internet_ip = m.get('InternetIp')

        if m.get('IntranetIp') is not None:
            self.intranet_ip = m.get('IntranetIp')

        if m.get('OtherId') is not None:
            self.other_id = m.get('OtherId')

        if m.get('Poc') is not None:
            self.poc = m.get('Poc')

        if m.get('PocCreateTime') is not None:
            self.poc_create_time = m.get('PocCreateTime')

        if m.get('PocDisclosureTime') is not None:
            self.poc_disclosure_time = m.get('PocDisclosureTime')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('Reference') is not None:
            self.reference = m.get('Reference')

        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')

        if m.get('Solution') is not None:
            self.solution = m.get('Solution')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        if m.get('VulLevel') is not None:
            self.vul_level = m.get('VulLevel')

        return self

class DescribeVulDetailsResponseBodyCvesClassifys(DaraModel):
    def __init__(
        self,
        classify: str = None,
        demo_video_url: str = None,
        description: str = None,
    ):
        # The type of the vulnerability.
        self.classify = classify
        # The URL of the demo video for the vulnerability.
        self.demo_video_url = demo_video_url
        # The description of the vulnerability type.
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.classify is not None:
            result['Classify'] = self.classify

        if self.demo_video_url is not None:
            result['DemoVideoUrl'] = self.demo_video_url

        if self.description is not None:
            result['Description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Classify') is not None:
            self.classify = m.get('Classify')

        if m.get('DemoVideoUrl') is not None:
            self.demo_video_url = m.get('DemoVideoUrl')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        return self

