# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVersionConfigResponseBody(DaraModel):
    def __init__(
        self,
        agentless_capacity: int = None,
        allow_partial_buy: int = None,
        anti_ransomware_capacity: int = None,
        anti_ransomware_service: int = None,
        app_white_list: int = None,
        app_white_list_auth_count: int = None,
        asset_level: int = None,
        can_try_post_paid_package: int = None,
        cspm_capacity: int = None,
        highest_version: int = None,
        honeypot_capacity: int = None,
        image_scan_capacity: int = None,
        instance_buy_type: int = None,
        instance_id: str = None,
        intelligent_analysis_flow: int = None,
        is_new_container_version: bool = None,
        is_new_multi_version: bool = None,
        is_over_balance: bool = None,
        is_postpay: bool = None,
        is_trial_version: int = None,
        last_trail_end_time: int = None,
        mvauth_count: int = None,
        mvunused_auth_count: int = None,
        merged_version: int = None,
        multi_version: str = None,
        new_threat_analysis: int = None,
        onboarded_assets: int = None,
        open_time: int = None,
        post_pay_host_version: int = None,
        post_pay_instance_id: str = None,
        post_pay_module_switch: str = None,
        post_pay_open_time: int = None,
        post_pay_status: int = None,
        rasp_capacity: int = None,
        release_time: int = None,
        request_id: str = None,
        sas_log: int = None,
        sas_screen: int = None,
        sdk_capacity: int = None,
        sls_capacity: int = None,
        threat_analysis_capacity: int = None,
        threat_analysis_flow: int = None,
        user_defined_alarms: int = None,
        version: int = None,
        vm_cores: int = None,
        vul_fix_capacity: int = None,
        web_lock: int = None,
        web_lock_auth_count: int = None,
    ):
        # Number of agentless detections. 
        # >Agentless detection is not yet available for sale, so there\\"s no need to pay attention to this field at the moment.
        self.agentless_capacity = agentless_capacity
        # Whether to allow pay-as-you-go purchases.
        # - **0**: Not allowed 
        # - **1**: Allowed
        self.allow_partial_buy = allow_partial_buy
        # Ransomware protection backup capacity, in GB.
        self.anti_ransomware_capacity = anti_ransomware_capacity
        # Ransomware Guardian Service. Values:
        #  - **0**: Not activated
        #  - **1**: Activated
        self.anti_ransomware_service = anti_ransomware_service
        # Whether to enable the application whitelist. Values: 
        # - **0**: Not enabled 
        # - **2**: Enabled
        self.app_white_list = app_white_list
        # Number of application whitelist authorizations. 
        # > One authorization allows the application of a whitelist policy to one server. After enabling the application whitelist function, the account will have 20 authorizations by default.
        self.app_white_list_auth_count = app_white_list_auth_count
        # Number of purchased server licenses.
        self.asset_level = asset_level
        # Whether it supports the activation of a post-paid trial package. Values: 
        # - **0**: Not supported
        #  - **1**: Supported
        self.can_try_post_paid_package = can_try_post_paid_package
        # Purchased cloud platform configuration check scan count. Unit: times/month.
        self.cspm_capacity = cspm_capacity
        # Purchase the highest version of the Security Center. Values:
        #  - **1**: Free Edition 
        # - **3**: Enterprise Edition 
        # - **5**: Advanced Edition 
        # - **6**: Anti-Virus Edition
        #  - **7**: Flagship Edition 
        # - **10**: Purchase Additional Services Only 
        # > When purchasing a single version, it indicates the corresponding version. When purchasing multiple versions, this value represents the highest version among the purchased multi-versions of Cloud Security Center.
        self.highest_version = highest_version
        # Number of purchased honeypot licenses.
        self.honeypot_capacity = honeypot_capacity
        # Number of purchased image scanning authorizations.
        self.image_scan_capacity = image_scan_capacity
        # Instance purchase type. Values: 
        # - **0**: Self-purchased
        #  - **1**: Allocated from multiple accounts
        self.instance_buy_type = instance_buy_type
        # ID of the purchased Cloud Security Center instance.
        self.instance_id = instance_id
        # AI digital human analyzes traffic
        self.intelligent_analysis_flow = intelligent_analysis_flow
        # Whether it is the new flagship version.
        # - **true**: It is the latest version
        # - **false**: It is not the latest version
        self.is_new_container_version = is_new_container_version
        # Whether it is the latest multi-version.
        # - **true**: It is the latest multi-version 
        # - **false**: It is not the latest multi-version
        self.is_new_multi_version = is_new_multi_version
        # Whether the number of existing servers exceeds the maximum authorized purchase quantity. Values: 
        # - **false**: Not exceeded 
        # - **true**: Exceeded
        # >Notice: This parameter is deprecated, and you do not need to pay attention to it.
        self.is_over_balance = is_over_balance
        # Whether to enable pay-as-you-go. Values: 
        # - **false**: Not enabled 
        # - **true**: Enabled
        self.is_postpay = is_postpay
        # Indicates whether the current Cloud Security Center version is a trial version. Values: 
        # - **0**: Not a trial version 
        # - **1**: Trial version
        self.is_trial_version = is_trial_version
        # The timestamp of the last trial expiration for Cloud Security Center, in milliseconds.
        self.last_trail_end_time = last_trail_end_time
        # Total number of licenses when purchasing multiple versions.
        self.mvauth_count = mvauth_count
        # Total remaining licenses when purchasing multiple versions.
        self.mvunused_auth_count = mvunused_auth_count
        # When both the annual/monthly and pay-as-you-go services for Cloud Security Center\\"s host and container security are activated, the higher protection version of the two is selected. Values: 
        # - **1**: Free Edition
        #  - **6**: Anti-Virus Edition 
        # - **5**: Advanced Edition 
        # - **3**: Enterprise Edition 
        # - **7**: Ultimate Edition
        self.merged_version = merged_version
        # Usage of multiple version numbers and license counts
        self.multi_version = multi_version
        # Whether to enable the new version of Threat Analysis and Response service. The new version of Threat Analysis and Response service refers to the one that supports purchasing access traffic and log storage capacity. Values: 
        # - **0**: No 
        # - **1**: Yes
        self.new_threat_analysis = new_threat_analysis
        # AI Digital Human Management Instance
        self.onboarded_assets = onboarded_assets
        # Service activation timestamp, unit: milliseconds.
        self.open_time = open_time
        # When activating the pay-as-you-go service for host and container security, it represents the highest protection version of the already bound assets. Values: 
        # - **1**: Free Edition
        #  - **3**: Enterprise Edition
        #  - **5**: Advanced Edition
        #  - **6**: Anti-Virus Edition 
        # - **7**: Flagship Edition
        self.post_pay_host_version = post_pay_host_version
        # Pay-As-You-Go instance ID.
        self.post_pay_instance_id = post_pay_instance_id
        # Pay-as-you-go module switch status, in the format of JsonString, with values as follows:
        #  - Key:
        #    * **VUL**: Vulnerability Repair Module 
        #    * **CSPM**: Cloud Security Posture Management Module 
        #    * **AGENTLESS**: Agentless Detection Module 
        #    * **SERVERLESS**: Serverless Security Module 
        #    * **CTDR**: Threat Analysis and Response Module 
        #    * **POST_HOST**: Host and Container Security Module 
        #    *  **SDK**: Malicious File Detection SDK Module 
        #    * **RASP**: Application Protection Module 
        #  - Value: 0 indicates off, 1 indicates on
        self.post_pay_module_switch = post_pay_module_switch
        # Pay-as-you-go activation time
        self.post_pay_open_time = post_pay_open_time
        # Pay-As-You-Go instance status. Values: 
        # - **1**: Normal 
        # - **2**: Stopped due to unpaid bills
        self.post_pay_status = post_pay_status
        # Number of purchased application protections. Unit: per month.
        self.rasp_capacity = rasp_capacity
        # The timestamp of when the Cloud Security Center instance will expire, in milliseconds.
        # > If you do not renew the service within 7 days after it expires, your paid instance will be downgraded to a free version, and you will no longer be able to use the features of the paid version. Your previous Cloud Security Center configuration data and historical alert data (e.g., DDoS alerts) will become inaccessible. At this point, you can only re-enable the paid version of Cloud Security Center by repurchasing it. For more information, see [Purchasing Cloud Security Center](https://help.aliyun.com/document_detail/42308.html).
        self.release_time = release_time
        # The unique identifier generated by Alibaba Cloud for this request.
        self.request_id = request_id
        # Whether log analysis has been purchased. Values: 
        # - **0**: Not purchased 
        # - **1**: Purchased
        self.sas_log = sas_log
        # Whether the security dashboard has been purchased. Values: 
        # - **0**: Not purchased 
        # - **1**: Purchased
        self.sas_screen = sas_screen
        # Number of SDK authorizations for malicious file detection
        self.sdk_capacity = sdk_capacity
        # Purchased log storage capacity in GB. Range: 0 to 200000.
        self.sls_capacity = sls_capacity
        # Purchased threat analysis capacity. Unit: GB.
        self.threat_analysis_capacity = threat_analysis_capacity
        # Purchased threat analysis and response log access traffic. Unit is GB/day.
        self.threat_analysis_flow = threat_analysis_flow
        # Whether to enable the custom alarm function. Values:
        #  - **0**: Not enabled 
        # - **2**: Enabled
        self.user_defined_alarms = user_defined_alarms
        # Purchased Cloud Security Center version. Values:   
        # - **1**: Free Edition 
        #  - **3**: Enterprise Edition 
        # - **5**: Advanced Edition 
        # - **6**: Anti-Virus Edition     
        # - **7**: Flagship Edition   
        #  - **8**: Multi-Edition  
        #   - **10**: Value-Added Services Only
        self.version = version
        # Number of authorized cores purchased.
        self.vm_cores = vm_cores
        # Number of purchased vulnerability fixes. Unit: times/month.
        self.vul_fix_capacity = vul_fix_capacity
        # Indicates whether the web tamper-proof service is enabled. Values: 
        # - **0**: Not enabled 
        # - **1**: Enabled
        self.web_lock = web_lock
        # The number of purchased web tamper-proof licenses. One license can enable web tamper protection for one server. Value range: 0~N.
        #  >N is the number of servers you have.
        self.web_lock_auth_count = web_lock_auth_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agentless_capacity is not None:
            result['AgentlessCapacity'] = self.agentless_capacity

        if self.allow_partial_buy is not None:
            result['AllowPartialBuy'] = self.allow_partial_buy

        if self.anti_ransomware_capacity is not None:
            result['AntiRansomwareCapacity'] = self.anti_ransomware_capacity

        if self.anti_ransomware_service is not None:
            result['AntiRansomwareService'] = self.anti_ransomware_service

        if self.app_white_list is not None:
            result['AppWhiteList'] = self.app_white_list

        if self.app_white_list_auth_count is not None:
            result['AppWhiteListAuthCount'] = self.app_white_list_auth_count

        if self.asset_level is not None:
            result['AssetLevel'] = self.asset_level

        if self.can_try_post_paid_package is not None:
            result['CanTryPostPaidPackage'] = self.can_try_post_paid_package

        if self.cspm_capacity is not None:
            result['CspmCapacity'] = self.cspm_capacity

        if self.highest_version is not None:
            result['HighestVersion'] = self.highest_version

        if self.honeypot_capacity is not None:
            result['HoneypotCapacity'] = self.honeypot_capacity

        if self.image_scan_capacity is not None:
            result['ImageScanCapacity'] = self.image_scan_capacity

        if self.instance_buy_type is not None:
            result['InstanceBuyType'] = self.instance_buy_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.intelligent_analysis_flow is not None:
            result['IntelligentAnalysisFlow'] = self.intelligent_analysis_flow

        if self.is_new_container_version is not None:
            result['IsNewContainerVersion'] = self.is_new_container_version

        if self.is_new_multi_version is not None:
            result['IsNewMultiVersion'] = self.is_new_multi_version

        if self.is_over_balance is not None:
            result['IsOverBalance'] = self.is_over_balance

        if self.is_postpay is not None:
            result['IsPostpay'] = self.is_postpay

        if self.is_trial_version is not None:
            result['IsTrialVersion'] = self.is_trial_version

        if self.last_trail_end_time is not None:
            result['LastTrailEndTime'] = self.last_trail_end_time

        if self.mvauth_count is not None:
            result['MVAuthCount'] = self.mvauth_count

        if self.mvunused_auth_count is not None:
            result['MVUnusedAuthCount'] = self.mvunused_auth_count

        if self.merged_version is not None:
            result['MergedVersion'] = self.merged_version

        if self.multi_version is not None:
            result['MultiVersion'] = self.multi_version

        if self.new_threat_analysis is not None:
            result['NewThreatAnalysis'] = self.new_threat_analysis

        if self.onboarded_assets is not None:
            result['OnboardedAssets'] = self.onboarded_assets

        if self.open_time is not None:
            result['OpenTime'] = self.open_time

        if self.post_pay_host_version is not None:
            result['PostPayHostVersion'] = self.post_pay_host_version

        if self.post_pay_instance_id is not None:
            result['PostPayInstanceId'] = self.post_pay_instance_id

        if self.post_pay_module_switch is not None:
            result['PostPayModuleSwitch'] = self.post_pay_module_switch

        if self.post_pay_open_time is not None:
            result['PostPayOpenTime'] = self.post_pay_open_time

        if self.post_pay_status is not None:
            result['PostPayStatus'] = self.post_pay_status

        if self.rasp_capacity is not None:
            result['RaspCapacity'] = self.rasp_capacity

        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sas_log is not None:
            result['SasLog'] = self.sas_log

        if self.sas_screen is not None:
            result['SasScreen'] = self.sas_screen

        if self.sdk_capacity is not None:
            result['SdkCapacity'] = self.sdk_capacity

        if self.sls_capacity is not None:
            result['SlsCapacity'] = self.sls_capacity

        if self.threat_analysis_capacity is not None:
            result['ThreatAnalysisCapacity'] = self.threat_analysis_capacity

        if self.threat_analysis_flow is not None:
            result['ThreatAnalysisFlow'] = self.threat_analysis_flow

        if self.user_defined_alarms is not None:
            result['UserDefinedAlarms'] = self.user_defined_alarms

        if self.version is not None:
            result['Version'] = self.version

        if self.vm_cores is not None:
            result['VmCores'] = self.vm_cores

        if self.vul_fix_capacity is not None:
            result['VulFixCapacity'] = self.vul_fix_capacity

        if self.web_lock is not None:
            result['WebLock'] = self.web_lock

        if self.web_lock_auth_count is not None:
            result['WebLockAuthCount'] = self.web_lock_auth_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentlessCapacity') is not None:
            self.agentless_capacity = m.get('AgentlessCapacity')

        if m.get('AllowPartialBuy') is not None:
            self.allow_partial_buy = m.get('AllowPartialBuy')

        if m.get('AntiRansomwareCapacity') is not None:
            self.anti_ransomware_capacity = m.get('AntiRansomwareCapacity')

        if m.get('AntiRansomwareService') is not None:
            self.anti_ransomware_service = m.get('AntiRansomwareService')

        if m.get('AppWhiteList') is not None:
            self.app_white_list = m.get('AppWhiteList')

        if m.get('AppWhiteListAuthCount') is not None:
            self.app_white_list_auth_count = m.get('AppWhiteListAuthCount')

        if m.get('AssetLevel') is not None:
            self.asset_level = m.get('AssetLevel')

        if m.get('CanTryPostPaidPackage') is not None:
            self.can_try_post_paid_package = m.get('CanTryPostPaidPackage')

        if m.get('CspmCapacity') is not None:
            self.cspm_capacity = m.get('CspmCapacity')

        if m.get('HighestVersion') is not None:
            self.highest_version = m.get('HighestVersion')

        if m.get('HoneypotCapacity') is not None:
            self.honeypot_capacity = m.get('HoneypotCapacity')

        if m.get('ImageScanCapacity') is not None:
            self.image_scan_capacity = m.get('ImageScanCapacity')

        if m.get('InstanceBuyType') is not None:
            self.instance_buy_type = m.get('InstanceBuyType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IntelligentAnalysisFlow') is not None:
            self.intelligent_analysis_flow = m.get('IntelligentAnalysisFlow')

        if m.get('IsNewContainerVersion') is not None:
            self.is_new_container_version = m.get('IsNewContainerVersion')

        if m.get('IsNewMultiVersion') is not None:
            self.is_new_multi_version = m.get('IsNewMultiVersion')

        if m.get('IsOverBalance') is not None:
            self.is_over_balance = m.get('IsOverBalance')

        if m.get('IsPostpay') is not None:
            self.is_postpay = m.get('IsPostpay')

        if m.get('IsTrialVersion') is not None:
            self.is_trial_version = m.get('IsTrialVersion')

        if m.get('LastTrailEndTime') is not None:
            self.last_trail_end_time = m.get('LastTrailEndTime')

        if m.get('MVAuthCount') is not None:
            self.mvauth_count = m.get('MVAuthCount')

        if m.get('MVUnusedAuthCount') is not None:
            self.mvunused_auth_count = m.get('MVUnusedAuthCount')

        if m.get('MergedVersion') is not None:
            self.merged_version = m.get('MergedVersion')

        if m.get('MultiVersion') is not None:
            self.multi_version = m.get('MultiVersion')

        if m.get('NewThreatAnalysis') is not None:
            self.new_threat_analysis = m.get('NewThreatAnalysis')

        if m.get('OnboardedAssets') is not None:
            self.onboarded_assets = m.get('OnboardedAssets')

        if m.get('OpenTime') is not None:
            self.open_time = m.get('OpenTime')

        if m.get('PostPayHostVersion') is not None:
            self.post_pay_host_version = m.get('PostPayHostVersion')

        if m.get('PostPayInstanceId') is not None:
            self.post_pay_instance_id = m.get('PostPayInstanceId')

        if m.get('PostPayModuleSwitch') is not None:
            self.post_pay_module_switch = m.get('PostPayModuleSwitch')

        if m.get('PostPayOpenTime') is not None:
            self.post_pay_open_time = m.get('PostPayOpenTime')

        if m.get('PostPayStatus') is not None:
            self.post_pay_status = m.get('PostPayStatus')

        if m.get('RaspCapacity') is not None:
            self.rasp_capacity = m.get('RaspCapacity')

        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SasLog') is not None:
            self.sas_log = m.get('SasLog')

        if m.get('SasScreen') is not None:
            self.sas_screen = m.get('SasScreen')

        if m.get('SdkCapacity') is not None:
            self.sdk_capacity = m.get('SdkCapacity')

        if m.get('SlsCapacity') is not None:
            self.sls_capacity = m.get('SlsCapacity')

        if m.get('ThreatAnalysisCapacity') is not None:
            self.threat_analysis_capacity = m.get('ThreatAnalysisCapacity')

        if m.get('ThreatAnalysisFlow') is not None:
            self.threat_analysis_flow = m.get('ThreatAnalysisFlow')

        if m.get('UserDefinedAlarms') is not None:
            self.user_defined_alarms = m.get('UserDefinedAlarms')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VmCores') is not None:
            self.vm_cores = m.get('VmCores')

        if m.get('VulFixCapacity') is not None:
            self.vul_fix_capacity = m.get('VulFixCapacity')

        if m.get('WebLock') is not None:
            self.web_lock = m.get('WebLock')

        if m.get('WebLockAuthCount') is not None:
            self.web_lock_auth_count = m.get('WebLockAuthCount')

        return self

