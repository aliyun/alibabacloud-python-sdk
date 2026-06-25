# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class DeployApplicationRequest(DaraModel):
    def __init__(
        self,
        acr_assume_role_arn: str = None,
        acr_instance_id: str = None,
        agent_version: str = None,
        alb_ingress_readiness_gate: str = None,
        app_id: str = None,
        associate_eip: bool = None,
        auto_enable_application_scaling_rule: bool = None,
        batch_wait_time: int = None,
        change_order_desc: str = None,
        command: str = None,
        command_args: str = None,
        config_map_mount_desc: str = None,
        cpu: int = None,
        custom_host_alias: str = None,
        custom_image_network_type: str = None,
        deploy: str = None,
        dotnet: str = None,
        edas_container_version: str = None,
        empty_dir_desc: str = None,
        enable_ahas: str = None,
        enable_cpu_burst: bool = None,
        enable_grey_tag_route: bool = None,
        enable_namespace_agent_version: bool = None,
        enable_new_arms: bool = None,
        enable_prometheus: bool = None,
        enable_sidecar_resource_isolated: bool = None,
        envs: str = None,
        gpu_config: str = None,
        html: str = None,
        image_pull_secrets: str = None,
        image_url: str = None,
        init_containers_config: List[main_models.InitContainerConfig] = None,
        jar_start_args: str = None,
        jar_start_options: str = None,
        jdk: str = None,
        kafka_configs: str = None,
        labels: Dict[str, str] = None,
        liveness: str = None,
        loki_configs: str = None,
        max_surge_instance_ratio: int = None,
        max_surge_instances: int = None,
        memory: int = None,
        micro_registration: str = None,
        micro_registration_config: str = None,
        microservice_engine_config: str = None,
        min_ready_instance_ratio: int = None,
        min_ready_instances: int = None,
        mount_desc: str = None,
        mount_host: str = None,
        nas_configs: str = None,
        nas_id: str = None,
        new_sae_version: str = None,
        oidc_role_name: str = None,
        oss_ak_id: str = None,
        oss_ak_secret: str = None,
        oss_mount_descs: str = None,
        package_type: str = None,
        package_url: str = None,
        package_version: str = None,
        php: str = None,
        php_arms_config_location: str = None,
        php_config: str = None,
        php_config_location: str = None,
        post_start: str = None,
        pre_stop: str = None,
        pvtz_discovery_svc: str = None,
        python: str = None,
        python_modules: str = None,
        readiness: str = None,
        replicas: int = None,
        secret_mount_desc: str = None,
        security_group_id: str = None,
        service_tags: str = None,
        sidecar_containers_config: List[main_models.SidecarContainerConfig] = None,
        sls_configs: str = None,
        sls_log_env_tags: str = None,
        startup_probe: str = None,
        swimlane_pvtz_discovery_svc: str = None,
        termination_grace_period_seconds: int = None,
        timezone: str = None,
        tomcat_config: str = None,
        update_strategy: str = None,
        v_switch_id: str = None,
        war_start_options: str = None,
        web_container: str = None,
    ):
        # The ARN of the RAM role required to pull images across accounts. For more information, see [Authorize cross-account image pulls using RAM roles](https://help.aliyun.com/document_detail/223585.html).
        self.acr_assume_role_arn = acr_assume_role_arn
        # The Container Registry Enterprise Edition instance ID. Required when **ImageUrl** is from Container Registry Enterprise Edition.
        self.acr_instance_id = acr_instance_id
        # The AliyunAgent version.
        self.agent_version = agent_version
        # The ALB gateway readiness gate configuration.
        self.alb_ingress_readiness_gate = alb_ingress_readiness_gate
        # The ID of the application to deploy.
        # 
        # This parameter is required.
        self.app_id = app_id
        # Whether to associate an EIP. Values:
        # 
        # - **true**: Associate.
        # 
        # - **false**: Do not associate.
        self.associate_eip = associate_eip
        # Whether to automatically enable application Auto Scaling rules. Values:
        # 
        # - **true**: Enable.
        # 
        # - **false**: Disable.
        self.auto_enable_application_scaling_rule = auto_enable_application_scaling_rule
        # The wait time between batches, in seconds.
        self.batch_wait_time = batch_wait_time
        # The description of the release task.
        self.change_order_desc = change_order_desc
        # The startup command for your image. This command must be an executable object inside the container. Example:
        # 
        # ```
        # command:
        #       - echo
        #       - abc
        #       - >
        #       - file0
        # ```
        # 
        # In this example, Command="echo" and `CommandArgs=["abc", ">", "file0"]`.
        self.command = command
        # The arguments for the startup command **Command**. Format:
        # 
        # `["a","b"]`
        # 
        # In the earlier example, `CommandArgs=["abc", ">", "file0"]`. The value `["abc", ">", "file0"]` must be converted to a string in JSON array format. Leave this field empty if no arguments are needed.
        self.command_args = command_args
        # The mount description for a **ConfigMap**. Use configuration items created on the namespace configuration page to inject configuration into your container. Parameters:
        # 
        # - **configMapId**: The ID of the ConfigMap instance. Get it by calling the [ListNamespacedConfigMaps](https://help.aliyun.com/document_detail/176917.html) API.
        # 
        # - **key**: The key.
        # 
        # > You can mount all keys by passing `sae-sys-configmap-all`.
        # 
        # - **mountPath**: The mount path.
        self.config_map_mount_desc = config_map_mount_desc
        # The CPU required per instance, in milliCPU. Cannot be zero. Supported fixed specifications:
        # 
        # - **500**
        # 
        # - **1000**
        # 
        # - **2000**
        # 
        # - **4000**
        # 
        # - **8000**
        # 
        # - **12000**
        # 
        # - **16000**
        # 
        # - **32000**
        self.cpu = cpu
        # Custom host mappings inside your container. Values:
        # 
        # - **hostName**: A domain name or hostname.
        # 
        # - **ip**: An IP address.
        self.custom_host_alias = custom_host_alias
        # The custom image type. Set to an empty string for non-custom images:
        # 
        # - internet: Public network image
        # 
        # - intranet: Private network image
        self.custom_image_network_type = custom_image_network_type
        # This parameter applies only to stopped applications. If you call **DeployApplication** on a running application, it deploys immediately.
        # 
        # - **true**: Default. Deploys immediately, applies the new configuration, and starts instances.
        # 
        # - **false**: Applies the new configuration only. Does not start application instances.
        self.deploy = deploy
        # The .NET framework version:
        # 
        # - .NET 3.1
        # 
        # - .NET 5.0
        # 
        # - .NET 6.0
        # 
        # - .NET 7.0
        # 
        # - .NET 8.0
        self.dotnet = dotnet
        # The version of the application runtime environment for HSF applications, such as Ali-Tomcat containers.
        self.edas_container_version = edas_container_version
        # The configuration for shared temporary storage.
        self.empty_dir_desc = empty_dir_desc
        # Whether to integrate with AHAS. Values:
        # 
        # - **true**: Integrate with AHAS.
        # 
        # - **false**: Do not integrate with AHAS.
        self.enable_ahas = enable_ahas
        # Whether to enable CPU Burst:
        # 
        # - true: Enable.
        # 
        # - false: Do not enable.
        self.enable_cpu_burst = enable_cpu_burst
        # Whether to enable traffic canary rules. These rules apply only to Spring Cloud and Dubbo applications. Values:
        # 
        # - **true**: Enable canary rules.
        # 
        # - **false**: Disable canary rules.
        self.enable_grey_tag_route = enable_grey_tag_route
        # Whether to reuse the namespace Agent version configuration.
        self.enable_namespace_agent_version = enable_namespace_agent_version
        # Whether to enable the new ARMS feature:
        # 
        # - true: Enable.
        # 
        # - false: Do not enable.
        self.enable_new_arms = enable_new_arms
        # Whether to enable Prometheus custom metric collection.
        self.enable_prometheus = enable_prometheus
        # Whether to isolate sidecar resources:
        # 
        # - true: Isolate.
        # 
        # - false: Do not isolate.
        self.enable_sidecar_resource_isolated = enable_sidecar_resource_isolated
        # The environment variables for your container. You can define custom variables or reference configuration items. To reference a configuration item, first create a ConfigMap instance. For more information, see [CreateConfigMap](https://help.aliyun.com/document_detail/176914.html). Values:
        # 
        # - Custom configuration
        # 
        #   - **name**: The name of the environment variable.
        # 
        #   - **value**: The value of the environment variable. Takes precedence over valueFrom.
        # 
        # - Reference a configuration item (valueFrom)
        # 
        #   - **name**: The name of the environment variable. You can reference a single key or all keys. To reference all keys, use `sae-sys-configmap-all-<configmap-name>`, for example `sae-sys-configmap-all-test1`.
        # 
        #   - **valueFrom**: The reference type. Set to `configMapRef`.
        # 
        #   - **configMapId**: The ID of the ConfigMap instance.
        # 
        #   - **key**: The key. Omit this field if you reference all keys.
        # 
        # - Reference a secret (valueFrom)
        # 
        #   - **name**: The name of the environment variable. You can reference a single key or all keys. To reference all keys, use `sae-sys-secret-all-<secret-name>`, for example `sae-sys-secret-all-test1`.
        # 
        #   - **valueFrom**: The reference type. Set to `secretRef`.
        # 
        #   - **secretId**: The ID of the secret.
        # 
        #   - **key**: The key. Omit this field if you reference all keys.
        self.envs = envs
        self.gpu_config = gpu_config
        # The Nginx version:
        # 
        # - nginx 1.20
        # 
        # - nginx 1.22
        # 
        # - nginx 1.24
        # 
        # - nginx 1.26
        # 
        # - nginx 1.28
        self.html = html
        # The ID of the corresponding secret.
        self.image_pull_secrets = image_pull_secrets
        # The registry address of your image. Required when **Package Type** is **Image**.
        self.image_url = image_url
        # The initialization container configuration.
        self.init_containers_config = init_containers_config
        # Startup arguments for your JAR package. Default startup command: `$JAVA_HOME/bin/java $JarStartOptions -jar $CATALINA_OPTS "$package_path" $JarStartArgs`
        self.jar_start_args = jar_start_args
        # Startup options for your JAR package. Default startup command: `$JAVA_HOME/bin/java $JarStartOptions -jar $CATALINA_OPTS "$package_path" $JarStartArgs`
        self.jar_start_options = jar_start_options
        # The JDK version that your deployment package depends on. Supported versions include the following:
        # 
        # - **Open JDK 8**
        # 
        # - **Open JDK 7**
        # 
        # - **Dragonwell 11**
        # 
        # - **Dragonwell 8**
        # 
        # - **openjdk-8u191-jdk-alpine3.9**
        # 
        # - **openjdk-7u201-jdk-alpine3.9**
        # 
        # This parameter is not supported when **Package Type** is **Image**.
        self.jdk = jdk
        # The configuration for collecting logs to Kafka. Values:
        # 
        # - **kafkaEndpoint**: The endpoint for the Kafka API.
        # 
        # - **kafkaInstanceId**: The Kafka instance ID.
        # 
        # - **kafkaConfigs**: The configuration for one or more log entries. For examples and details, see the \\*\\*kafkaConfigs\\*\\* request parameter in this topic.
        self.kafka_configs = kafka_configs
        self.labels = labels
        # Health checks for your container. Containers that fail health checks are terminated and restarted. Supported methods:
        # 
        # - **exec**: For example, `{"exec":{"command":["sh","-c","cat/home/admin/start.sh"]},"initialDelaySeconds":30,"periodSeconds":30,"timeoutSeconds":2}`
        # 
        # - **httpGet**: For example, `{"httpGet":{"path":"/","port":18091,"scheme":"HTTP","isContainKeyWord":true,"keyWord":"SAE"},"initialDelaySeconds":11,"periodSeconds":10,"timeoutSeconds":1}`
        # 
        # - **tcpSocket**: For example, `{"tcpSocket":{"port":18091},"initialDelaySeconds":11,"periodSeconds":10,"timeoutSeconds":1}`
        # 
        # > You can select only one health check method.
        # 
        # Parameters:
        # 
        # - **exec.command**: The health check command.
        # 
        # - **httpGet.path**: The path to access.
        # 
        # - **httpGet.scheme**: **HTTP** or **HTTPS**.
        # 
        # - **httpGet.isContainKeyWord**: **true** means the response contains a keyword. **false** means it does not. If omitted, advanced features are disabled.
        # 
        # - **httpGet.keyWord**: Your custom keyword. Include **isContainKeyWord** when using this field.
        # 
        # - **tcpSocket.port**: The port for TCP connection checks.
        # 
        # - **initialDelaySeconds**: The delay before the first health check, in seconds. Default is 10.
        # 
        # - **periodSeconds**: The interval between health checks, in seconds. Default is 30.
        # 
        # - **timeoutSeconds**: The timeout for each health check, in seconds. Default is 1. If set to 0 or omitted, the default is 1 second.
        self.liveness = liveness
        self.loki_configs = loki_configs
        # The maximum number of surge instances as a percentage of total instances. Values:
        # 
        # If the minimum available instances is 100%, the maximum surge cannot be set to 0. If set to -1, the system uses its recommended value: 30% of your current instance count. For example, with 10 instances, 10 × 30% = 3.
        self.max_surge_instance_ratio = max_surge_instance_ratio
        # The maximum number of surge instances during a rolling update. Values:
        # 
        # If the minimum available instances is 100%, the maximum surge cannot be set to 0. If set to -1, the system uses its recommended value: 30% of your current instance count. For example, with 10 instances, 10 × 30% = 3.
        self.max_surge_instances = max_surge_instances
        # The memory required per instance, in MB. Cannot be zero. Memory and CPU are paired. Supported fixed specifications:
        # 
        # - **1024**: Pairs with 500 and 1000 milliCPU.
        # 
        # - **2048**: Pairs with 500, 1000, and 2000 milliCPU.
        # 
        # - **4096**: Pairs with 1000, 2000, and 4000 milliCPU.
        # 
        # - **8192**: Pairs with 2000, 4000, and 8000 milliCPU.
        # 
        # - **12288**: Pairs with 12000 milliCPU.
        # 
        # - **16384**: Pairs with 4000, 8000, and 16000 milliCPU.
        # 
        # - **24576**: Pairs with 12000 milliCPU.
        # 
        # - **32768**: Pairs with 16000 milliCPU.
        # 
        # - **65536**: Pairs with 8000, 16000, and 32000 milliCPU.
        # 
        # - **131072**: Pairs with 32000 milliCPU.
        self.memory = memory
        # Select a Nacos registry center. Values:
        # 
        # - **0**: Built-in Nacos in SAE.
        # 
        # - **1**: Self-managed Nacos.
        # 
        # - **2**: MSE Nacos Commercial Edition.
        # 
        # > If you select built-in Nacos in SAE, you cannot retrieve its configuration.
        self.micro_registration = micro_registration
        # The registry configuration. Applies only when the registry type is MSE Nacos Enterprise Edition.
        self.micro_registration_config = micro_registration_config
        # Configure microservice governance features.
        # 
        # - Enable microservice governance (enable):
        # 
        #   - true: Enable
        # 
        #   - false: Disable
        # 
        # - Configure graceful start and shutdown (mseLosslessRule):
        # 
        #   - delayTime: Delay time
        # 
        #   - enable: Whether to enable graceful start. true enables it. false disables it.
        # 
        #   - notice: Whether to enable notifications. true enables them. false disables them.
        # 
        #   - warmupTime: Warm-up duration for small traffic, in seconds.
        self.microservice_engine_config = microservice_engine_config
        # The minimum number of available instances as a percentage of total instances. Values:
        # 
        # - **-1**: Use the default value. No percentage is applied.
        # 
        # - **0–100**: Percentage value. Rounded up. For example, if set to **50**% and you have 5 instances, the minimum is 3.
        # 
        # > If both **MinReadyInstances** and **MinReadyInstanceRatio** are provided, and **MinReadyInstanceRatio** is not **-1**, then **MinReadyInstanceRatio** takes precedence. For example, if **MinReadyInstances** is **5** and **MinReadyInstanceRatio** is **50**, the system calculates the minimum based on 50%.
        self.min_ready_instance_ratio = min_ready_instance_ratio
        # The minimum number of instances that remain available during a rolling update. Values:
        # 
        # - If set to **0**, your application experiences downtime during updates.
        # 
        # - If set to -1, the system uses its recommended value: 25% of your current instance count. For example, with 5 instances, 5 × 25% = 1.25, rounded up to 2.
        # 
        # > We recommend setting this value to at least 1 to avoid service interruptions.
        self.min_ready_instances = min_ready_instances
        # We recommend using **NasConfigs** instead of this field. The NAS mount description. If your NAS configuration remains unchanged, omit this parameter. To clear your NAS configuration, set this field to an empty string.
        self.mount_desc = mount_desc
        # We recommend using **NasConfigs** instead of this field. The mount target of the NAS in your application\\"s VPC. If your NAS configuration remains unchanged, omit this parameter. To clear your NAS configuration, set this field to an empty string.
        self.mount_host = mount_host
        # The configuration for mounting NAS. Values:
        # 
        # - **mountPath**: The mount path in the container.
        # 
        # - **readOnly**: Set to **false** for read and write permissions.
        # 
        # - **nasId**: The NAS ID.
        # 
        # - **mountDomain**: The mount target address. For more information, see [DescribeMountTargets](https://help.aliyun.com/document_detail/62626.html).
        # 
        # - **nasPath**: The relative directory in NAS.
        self.nas_configs = nas_configs
        # We recommend using **NasConfigs** instead of this field. The ID of the NAS file system. If your NAS configuration remains unchanged, omit this parameter. To clear your NAS configuration, set this field to an empty string.
        self.nas_id = nas_id
        # The application version:
        # 
        # - lite: Lite Edition
        # 
        # - std: Standard Edition
        # 
        # - pro: Professional Edition
        self.new_sae_version = new_sae_version
        # The RAM role for identity authentication.
        # 
        # > Create an OIDC identity provider and an associated role in the same region before using this parameter. For more information, see [Create an OIDC identity provider](https://help.aliyun.com/document_detail/2331022.html) and [Create a role for SSO identity providers](https://help.aliyun.com/document_detail/2331016.html).
        self.oidc_role_name = oidc_role_name
        # The AccessKey ID for OSS read and write operations.
        self.oss_ak_id = oss_ak_id
        # The AccessKey secret for OSS read and write operations.
        self.oss_ak_secret = oss_ak_secret
        # The OSS mount description. Parameters:
        # 
        # - **bucketName**: The name of the bucket.
        # 
        # - **bucketPath**: The directory or object in OSS. If the directory does not exist, an error occurs.
        # 
        # - **mountPath**: The path in your SAE container. If the path exists, it is overwritten. If it does not exist, it is created.
        # 
        # - **readOnly**: Whether the container path has read-only access to the mounted resource. Values:
        # 
        #   - **true**: Read-only.
        # 
        #   - **false**: Read and write.
        self.oss_mount_descs = oss_mount_descs
        # The type of your application package. Values:
        # 
        # - For Java applications: **FatJar**, **War**, and **Image**.
        # 
        # - For PHP applications:
        # 
        #   - **PhpZip**
        # 
        #   - **IMAGE_PHP_5_4**
        # 
        #   - **IMAGE_PHP_5_4_ALPINE**
        # 
        #   - **IMAGE_PHP_5_5**
        # 
        #   - **IMAGE_PHP_5_5_ALPINE**
        # 
        #   - **IMAGE_PHP_5_6**
        # 
        #   - **IMAGE_PHP_5_6_ALPINE**
        # 
        #   - **IMAGE_PHP_7_0**
        # 
        #   - **IMAGE_PHP_7_0_ALPINE**
        # 
        #   - **IMAGE_PHP_7_1**
        # 
        #   - **IMAGE_PHP_7_1_ALPINE**
        # 
        #   - **IMAGE_PHP_7_2**
        # 
        #   - **IMAGE_PHP_7_2_ALPINE**
        # 
        #   - **IMAGE_PHP_7_3**
        # 
        #   - **IMAGE_PHP_7_3_ALPINE**
        # 
        # - For Python applications: **PythonZip** and **Image**.
        self.package_type = package_type
        # The URL of your deployment package. Required when **Package Type** is **FatJar**, **War**, or **PythonZip**.
        self.package_url = package_url
        # The version number of your deployment package. Required when **Package Type** is **FatJar**, **War**, or **PythonZip**.
        self.package_version = package_version
        # The PHP version that your PHP deployment package depends on. Not supported for images.
        self.php = php
        # The mount path for PHP application monitoring. Ensure your PHP server loads the configuration file at this path. You do not need to manage the configuration content. SAE renders the correct configuration automatically.
        self.php_arms_config_location = php_arms_config_location
        # The content of the PHP configuration file.
        self.php_config = php_config
        # The mount path for the PHP startup configuration. Ensure your PHP server uses this configuration file to start.
        self.php_config_location = php_config_location
        # A script that runs after your container starts. It executes immediately after the container is created. Format: `{"exec":{"command":["sh","-c","echo hello"]}}`
        self.post_start = post_start
        # A script that runs before your container stops. It executes just before the container is deleted. Format: `{"exec":{"command":["sh","-c","echo hello"]}}`
        self.pre_stop = pre_stop
        # Enable K8s Service registration and discovery. Values:
        # 
        # - **portProtocols**: Port and protocol. Port range is [1,65535]. Protocols supported: **TCP** and **UDP**.
        # 
        # - portAndProtocol: Port and protocol. Port range is [1,65535]. Protocols supported: **TCP** and **UDP**. **portProtocols** takes precedence. If both are set, only **portProtocols** applies.
        # 
        # - **enable**: Enable K8s Service registration and discovery.
        self.pvtz_discovery_svc = pvtz_discovery_svc
        # The Python runtime environment. Supported: **PYTHON 3.9.15**.
        self.python = python
        # Custom module dependencies. By default, dependencies defined in requirements.txt in the root directory are installed. If no configuration or custom packages exist, specify the dependencies to install.
        self.python_modules = python_modules
        # Startup status checks for your application. Containers that repeatedly fail readiness checks are terminated and restarted. Containers that fail readiness checks receive no SLB traffic. Supports **exec**, **httpGet**, and **tcpSocket**. For examples, see the **Liveness** parameter.
        # 
        # > You can select only one health check method.
        self.readiness = readiness
        # The number of instances.
        self.replicas = replicas
        # The mount description for a **Secret**. Use secrets created on the namespace secrets page to inject sensitive information into your container. Parameters:
        # 
        # - **secretId**: The ID of the secret instance. Get it by calling the ListSecrets API.
        # 
        # - **key**: The key.
        # 
        # > You can mount all keys by passing `sae-sys-secret-all`.
        # 
        # - **mountPath**: The mount path.
        self.secret_mount_desc = secret_mount_desc
        # The security group ID.
        self.security_group_id = security_group_id
        # The canary tags configured for your application.
        self.service_tags = service_tags
        # Container configuration information.
        self.sidecar_containers_config = sidecar_containers_config
        # The configuration for collecting logs to Simple Log Service (SLS).
        # 
        # - Using SAE-managed SLS resources: `[{"logDir":"","logType":"stdout"},{"logDir":"/tmp/a.log"}]`.
        # 
        # - Using custom SLS resources: `[{"projectName":"test-sls","logType":"stdout","logDir":"","logstoreName":"sae","logtailName":""},{"projectName":"test","logDir":"/tmp/a.log","logstoreName":"sae","logtailName":""}]`.
        # 
        # Parameters:
        # 
        # - **projectName**: The name of the SLS project.
        # 
        # - **logDir**: The log file path.
        # 
        # - logType: The log type. **stdout** means standard output logs from the container. Only one **stdout** entry is allowed. If omitted, file logs are collected.
        # 
        # - **logstoreName**: The name of the SLS Logstore.
        # 
        # - **logtailName**: The name of the SLS Logtail. If omitted, a new Logtail is created.
        # 
        # If your SLS collection configuration remains unchanged across deployments, omit this parameter. To disable SLS collection, set this field to an empty string.
        # 
        # > Projects automatically created by SAE are deleted when the application is deleted. Do not select these projects when choosing an existing project.
        self.sls_configs = sls_configs
        # The SLS log tags.
        self.sls_log_env_tags = sls_log_env_tags
        # Enable application startup probing.
        # 
        # - Success: The application starts successfully. If you configure Liveness and Readiness checks, they run after startup.
        # 
        # - Failure: The application fails to start. SAE reports an error and restarts the container automatically.
        # 
        # > Description
        # >
        # > - Supports exec, httpGet, and tcpSocket. For examples, see the Liveness parameter.
        # >
        # > - You can select only one health check method.
        self.startup_probe = startup_probe
        # Configures service discovery and end-to-end canary release based on a Kubernetes Service:
        # 
        # - enable: Specifies whether to enable the end-to-end canary release feature.
        # 
        #   - true: Enables the feature.
        # 
        #   - false: Disables the feature.
        # 
        # - namespaceId: The namespace ID.
        # 
        # - portAndProtocol: The listening port and protocol. The format is {"\\<port>:\\<protocol>":"\\<target_port>"}.
        # 
        # - portProtocols: A list of ports and protocols for the service.
        # 
        #   - port: The port number.
        # 
        #   - protocol: The protocol.
        # 
        #   - targetPort: The container port.
        # 
        # - pvtzDiscoveryName: The service discovery name.
        # 
        # - serviceId: The service ID.
        # 
        # - serviceName: The service name.
        self.swimlane_pvtz_discovery_svc = swimlane_pvtz_discovery_svc
        # The graceful shutdown timeout, in seconds. Default is 30. Valid values: 1–300.
        self.termination_grace_period_seconds = termination_grace_period_seconds
        # The time zone. Default is **Asia/Shanghai**.
        self.timezone = timezone
        # The Tomcat configuration. Set to an empty string or {} to delete the configuration. Values:
        # 
        # - **port**: Port range is 1024–65535. Ports below 1024 require root privileges. Because containers run with admin privileges, use ports above 1024. Default is 8080.
        # 
        # - **contextPath**: The access path. Default is the root directory /.
        # 
        # - **maxThreads**: The size of the connection pool. Default is 400.
        # 
        # - uriEncoding: The encoding format for Tomcat. Options include **UTF-8**, **ISO-8859-1**, **GBK**, and **GB2312**. Default is **ISO-8859-1**.
        # 
        # - **useBodyEncodingForUri**: Whether to use body encoding for URLs. Default is **true**.
        self.tomcat_config = tomcat_config
        # The release strategy. When MinReadyInstances equals 1, set UpdateStrategy to an empty string. When **MinReadyInstances** is greater than 1, examples include the following:
        # 
        # - Canary release with 1 instance, followed by 2 automatic batches with a 1-minute interval: `{"type":"GrayBatchUpdate","batchUpdate":{"batch":2,"releaseType":"auto","batchWaitTime":1},"grayUpdate":{"gray":1}}`
        # 
        # - Canary release with 1 instance, followed by 2 manual batches: `{"type":"GrayBatchUpdate","batchUpdate":{"batch":2,"releaseType":"manual"},"grayUpdate":{"gray":1}}`
        # 
        # - Two automatic batches with a 0-minute interval: `{"type":"BatchUpdate","batchUpdate":{"batch":2,"releaseType":"auto","batchWaitTime":0}}`
        # 
        # Parameters:
        # 
        # - **type**: The release strategy type. Options are **GrayBatchUpdate** (canary release) or **BatchUpdate** (phased release).
        # 
        # - **batchUpdate**: The phased release strategy.
        # 
        #   - **batch**: The number of batches.
        # 
        #   - **releaseType**: How batches are processed. Options are **auto** (automatic) or **manual** (manual).
        # 
        #   - **batchWaitTime**: The wait time between batches, in minutes.
        # 
        # - **grayUpdate**: The number of canary instances. Required when **type** is **GrayBatchUpdate**.
        self.update_strategy = update_strategy
        # The virtual switch where your application instance elastic network interfaces reside. This switch must be in the specified VPC.
        self.v_switch_id = v_switch_id
        # The startup command for your WAR package. Configure it the same way as the startup command for images. For more information, see [Set the startup command](https://help.aliyun.com/document_detail/96677.html).
        self.war_start_options = war_start_options
        # The Tomcat version that your deployment package depends on. Supported versions include the following:
        # 
        # - **apache-tomcat-7.0.91**
        # 
        # - **apache-tomcat-8.5.42**
        # 
        # This parameter is not supported when **Package Type** is **Image**.
        self.web_container = web_container

    def validate(self):
        if self.init_containers_config:
            for v1 in self.init_containers_config:
                 if v1:
                    v1.validate()
        if self.sidecar_containers_config:
            for v1 in self.sidecar_containers_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acr_assume_role_arn is not None:
            result['AcrAssumeRoleArn'] = self.acr_assume_role_arn

        if self.acr_instance_id is not None:
            result['AcrInstanceId'] = self.acr_instance_id

        if self.agent_version is not None:
            result['AgentVersion'] = self.agent_version

        if self.alb_ingress_readiness_gate is not None:
            result['AlbIngressReadinessGate'] = self.alb_ingress_readiness_gate

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.associate_eip is not None:
            result['AssociateEip'] = self.associate_eip

        if self.auto_enable_application_scaling_rule is not None:
            result['AutoEnableApplicationScalingRule'] = self.auto_enable_application_scaling_rule

        if self.batch_wait_time is not None:
            result['BatchWaitTime'] = self.batch_wait_time

        if self.change_order_desc is not None:
            result['ChangeOrderDesc'] = self.change_order_desc

        if self.command is not None:
            result['Command'] = self.command

        if self.command_args is not None:
            result['CommandArgs'] = self.command_args

        if self.config_map_mount_desc is not None:
            result['ConfigMapMountDesc'] = self.config_map_mount_desc

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.custom_host_alias is not None:
            result['CustomHostAlias'] = self.custom_host_alias

        if self.custom_image_network_type is not None:
            result['CustomImageNetworkType'] = self.custom_image_network_type

        if self.deploy is not None:
            result['Deploy'] = self.deploy

        if self.dotnet is not None:
            result['Dotnet'] = self.dotnet

        if self.edas_container_version is not None:
            result['EdasContainerVersion'] = self.edas_container_version

        if self.empty_dir_desc is not None:
            result['EmptyDirDesc'] = self.empty_dir_desc

        if self.enable_ahas is not None:
            result['EnableAhas'] = self.enable_ahas

        if self.enable_cpu_burst is not None:
            result['EnableCpuBurst'] = self.enable_cpu_burst

        if self.enable_grey_tag_route is not None:
            result['EnableGreyTagRoute'] = self.enable_grey_tag_route

        if self.enable_namespace_agent_version is not None:
            result['EnableNamespaceAgentVersion'] = self.enable_namespace_agent_version

        if self.enable_new_arms is not None:
            result['EnableNewArms'] = self.enable_new_arms

        if self.enable_prometheus is not None:
            result['EnablePrometheus'] = self.enable_prometheus

        if self.enable_sidecar_resource_isolated is not None:
            result['EnableSidecarResourceIsolated'] = self.enable_sidecar_resource_isolated

        if self.envs is not None:
            result['Envs'] = self.envs

        if self.gpu_config is not None:
            result['GpuConfig'] = self.gpu_config

        if self.html is not None:
            result['Html'] = self.html

        if self.image_pull_secrets is not None:
            result['ImagePullSecrets'] = self.image_pull_secrets

        if self.image_url is not None:
            result['ImageUrl'] = self.image_url

        result['InitContainersConfig'] = []
        if self.init_containers_config is not None:
            for k1 in self.init_containers_config:
                result['InitContainersConfig'].append(k1.to_map() if k1 else None)

        if self.jar_start_args is not None:
            result['JarStartArgs'] = self.jar_start_args

        if self.jar_start_options is not None:
            result['JarStartOptions'] = self.jar_start_options

        if self.jdk is not None:
            result['Jdk'] = self.jdk

        if self.kafka_configs is not None:
            result['KafkaConfigs'] = self.kafka_configs

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.liveness is not None:
            result['Liveness'] = self.liveness

        if self.loki_configs is not None:
            result['LokiConfigs'] = self.loki_configs

        if self.max_surge_instance_ratio is not None:
            result['MaxSurgeInstanceRatio'] = self.max_surge_instance_ratio

        if self.max_surge_instances is not None:
            result['MaxSurgeInstances'] = self.max_surge_instances

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.micro_registration is not None:
            result['MicroRegistration'] = self.micro_registration

        if self.micro_registration_config is not None:
            result['MicroRegistrationConfig'] = self.micro_registration_config

        if self.microservice_engine_config is not None:
            result['MicroserviceEngineConfig'] = self.microservice_engine_config

        if self.min_ready_instance_ratio is not None:
            result['MinReadyInstanceRatio'] = self.min_ready_instance_ratio

        if self.min_ready_instances is not None:
            result['MinReadyInstances'] = self.min_ready_instances

        if self.mount_desc is not None:
            result['MountDesc'] = self.mount_desc

        if self.mount_host is not None:
            result['MountHost'] = self.mount_host

        if self.nas_configs is not None:
            result['NasConfigs'] = self.nas_configs

        if self.nas_id is not None:
            result['NasId'] = self.nas_id

        if self.new_sae_version is not None:
            result['NewSaeVersion'] = self.new_sae_version

        if self.oidc_role_name is not None:
            result['OidcRoleName'] = self.oidc_role_name

        if self.oss_ak_id is not None:
            result['OssAkId'] = self.oss_ak_id

        if self.oss_ak_secret is not None:
            result['OssAkSecret'] = self.oss_ak_secret

        if self.oss_mount_descs is not None:
            result['OssMountDescs'] = self.oss_mount_descs

        if self.package_type is not None:
            result['PackageType'] = self.package_type

        if self.package_url is not None:
            result['PackageUrl'] = self.package_url

        if self.package_version is not None:
            result['PackageVersion'] = self.package_version

        if self.php is not None:
            result['Php'] = self.php

        if self.php_arms_config_location is not None:
            result['PhpArmsConfigLocation'] = self.php_arms_config_location

        if self.php_config is not None:
            result['PhpConfig'] = self.php_config

        if self.php_config_location is not None:
            result['PhpConfigLocation'] = self.php_config_location

        if self.post_start is not None:
            result['PostStart'] = self.post_start

        if self.pre_stop is not None:
            result['PreStop'] = self.pre_stop

        if self.pvtz_discovery_svc is not None:
            result['PvtzDiscoverySvc'] = self.pvtz_discovery_svc

        if self.python is not None:
            result['Python'] = self.python

        if self.python_modules is not None:
            result['PythonModules'] = self.python_modules

        if self.readiness is not None:
            result['Readiness'] = self.readiness

        if self.replicas is not None:
            result['Replicas'] = self.replicas

        if self.secret_mount_desc is not None:
            result['SecretMountDesc'] = self.secret_mount_desc

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.service_tags is not None:
            result['ServiceTags'] = self.service_tags

        result['SidecarContainersConfig'] = []
        if self.sidecar_containers_config is not None:
            for k1 in self.sidecar_containers_config:
                result['SidecarContainersConfig'].append(k1.to_map() if k1 else None)

        if self.sls_configs is not None:
            result['SlsConfigs'] = self.sls_configs

        if self.sls_log_env_tags is not None:
            result['SlsLogEnvTags'] = self.sls_log_env_tags

        if self.startup_probe is not None:
            result['StartupProbe'] = self.startup_probe

        if self.swimlane_pvtz_discovery_svc is not None:
            result['SwimlanePvtzDiscoverySvc'] = self.swimlane_pvtz_discovery_svc

        if self.termination_grace_period_seconds is not None:
            result['TerminationGracePeriodSeconds'] = self.termination_grace_period_seconds

        if self.timezone is not None:
            result['Timezone'] = self.timezone

        if self.tomcat_config is not None:
            result['TomcatConfig'] = self.tomcat_config

        if self.update_strategy is not None:
            result['UpdateStrategy'] = self.update_strategy

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.war_start_options is not None:
            result['WarStartOptions'] = self.war_start_options

        if self.web_container is not None:
            result['WebContainer'] = self.web_container

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcrAssumeRoleArn') is not None:
            self.acr_assume_role_arn = m.get('AcrAssumeRoleArn')

        if m.get('AcrInstanceId') is not None:
            self.acr_instance_id = m.get('AcrInstanceId')

        if m.get('AgentVersion') is not None:
            self.agent_version = m.get('AgentVersion')

        if m.get('AlbIngressReadinessGate') is not None:
            self.alb_ingress_readiness_gate = m.get('AlbIngressReadinessGate')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AssociateEip') is not None:
            self.associate_eip = m.get('AssociateEip')

        if m.get('AutoEnableApplicationScalingRule') is not None:
            self.auto_enable_application_scaling_rule = m.get('AutoEnableApplicationScalingRule')

        if m.get('BatchWaitTime') is not None:
            self.batch_wait_time = m.get('BatchWaitTime')

        if m.get('ChangeOrderDesc') is not None:
            self.change_order_desc = m.get('ChangeOrderDesc')

        if m.get('Command') is not None:
            self.command = m.get('Command')

        if m.get('CommandArgs') is not None:
            self.command_args = m.get('CommandArgs')

        if m.get('ConfigMapMountDesc') is not None:
            self.config_map_mount_desc = m.get('ConfigMapMountDesc')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CustomHostAlias') is not None:
            self.custom_host_alias = m.get('CustomHostAlias')

        if m.get('CustomImageNetworkType') is not None:
            self.custom_image_network_type = m.get('CustomImageNetworkType')

        if m.get('Deploy') is not None:
            self.deploy = m.get('Deploy')

        if m.get('Dotnet') is not None:
            self.dotnet = m.get('Dotnet')

        if m.get('EdasContainerVersion') is not None:
            self.edas_container_version = m.get('EdasContainerVersion')

        if m.get('EmptyDirDesc') is not None:
            self.empty_dir_desc = m.get('EmptyDirDesc')

        if m.get('EnableAhas') is not None:
            self.enable_ahas = m.get('EnableAhas')

        if m.get('EnableCpuBurst') is not None:
            self.enable_cpu_burst = m.get('EnableCpuBurst')

        if m.get('EnableGreyTagRoute') is not None:
            self.enable_grey_tag_route = m.get('EnableGreyTagRoute')

        if m.get('EnableNamespaceAgentVersion') is not None:
            self.enable_namespace_agent_version = m.get('EnableNamespaceAgentVersion')

        if m.get('EnableNewArms') is not None:
            self.enable_new_arms = m.get('EnableNewArms')

        if m.get('EnablePrometheus') is not None:
            self.enable_prometheus = m.get('EnablePrometheus')

        if m.get('EnableSidecarResourceIsolated') is not None:
            self.enable_sidecar_resource_isolated = m.get('EnableSidecarResourceIsolated')

        if m.get('Envs') is not None:
            self.envs = m.get('Envs')

        if m.get('GpuConfig') is not None:
            self.gpu_config = m.get('GpuConfig')

        if m.get('Html') is not None:
            self.html = m.get('Html')

        if m.get('ImagePullSecrets') is not None:
            self.image_pull_secrets = m.get('ImagePullSecrets')

        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')

        self.init_containers_config = []
        if m.get('InitContainersConfig') is not None:
            for k1 in m.get('InitContainersConfig'):
                temp_model = main_models.InitContainerConfig()
                self.init_containers_config.append(temp_model.from_map(k1))

        if m.get('JarStartArgs') is not None:
            self.jar_start_args = m.get('JarStartArgs')

        if m.get('JarStartOptions') is not None:
            self.jar_start_options = m.get('JarStartOptions')

        if m.get('Jdk') is not None:
            self.jdk = m.get('Jdk')

        if m.get('KafkaConfigs') is not None:
            self.kafka_configs = m.get('KafkaConfigs')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('Liveness') is not None:
            self.liveness = m.get('Liveness')

        if m.get('LokiConfigs') is not None:
            self.loki_configs = m.get('LokiConfigs')

        if m.get('MaxSurgeInstanceRatio') is not None:
            self.max_surge_instance_ratio = m.get('MaxSurgeInstanceRatio')

        if m.get('MaxSurgeInstances') is not None:
            self.max_surge_instances = m.get('MaxSurgeInstances')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('MicroRegistration') is not None:
            self.micro_registration = m.get('MicroRegistration')

        if m.get('MicroRegistrationConfig') is not None:
            self.micro_registration_config = m.get('MicroRegistrationConfig')

        if m.get('MicroserviceEngineConfig') is not None:
            self.microservice_engine_config = m.get('MicroserviceEngineConfig')

        if m.get('MinReadyInstanceRatio') is not None:
            self.min_ready_instance_ratio = m.get('MinReadyInstanceRatio')

        if m.get('MinReadyInstances') is not None:
            self.min_ready_instances = m.get('MinReadyInstances')

        if m.get('MountDesc') is not None:
            self.mount_desc = m.get('MountDesc')

        if m.get('MountHost') is not None:
            self.mount_host = m.get('MountHost')

        if m.get('NasConfigs') is not None:
            self.nas_configs = m.get('NasConfigs')

        if m.get('NasId') is not None:
            self.nas_id = m.get('NasId')

        if m.get('NewSaeVersion') is not None:
            self.new_sae_version = m.get('NewSaeVersion')

        if m.get('OidcRoleName') is not None:
            self.oidc_role_name = m.get('OidcRoleName')

        if m.get('OssAkId') is not None:
            self.oss_ak_id = m.get('OssAkId')

        if m.get('OssAkSecret') is not None:
            self.oss_ak_secret = m.get('OssAkSecret')

        if m.get('OssMountDescs') is not None:
            self.oss_mount_descs = m.get('OssMountDescs')

        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')

        if m.get('PackageUrl') is not None:
            self.package_url = m.get('PackageUrl')

        if m.get('PackageVersion') is not None:
            self.package_version = m.get('PackageVersion')

        if m.get('Php') is not None:
            self.php = m.get('Php')

        if m.get('PhpArmsConfigLocation') is not None:
            self.php_arms_config_location = m.get('PhpArmsConfigLocation')

        if m.get('PhpConfig') is not None:
            self.php_config = m.get('PhpConfig')

        if m.get('PhpConfigLocation') is not None:
            self.php_config_location = m.get('PhpConfigLocation')

        if m.get('PostStart') is not None:
            self.post_start = m.get('PostStart')

        if m.get('PreStop') is not None:
            self.pre_stop = m.get('PreStop')

        if m.get('PvtzDiscoverySvc') is not None:
            self.pvtz_discovery_svc = m.get('PvtzDiscoverySvc')

        if m.get('Python') is not None:
            self.python = m.get('Python')

        if m.get('PythonModules') is not None:
            self.python_modules = m.get('PythonModules')

        if m.get('Readiness') is not None:
            self.readiness = m.get('Readiness')

        if m.get('Replicas') is not None:
            self.replicas = m.get('Replicas')

        if m.get('SecretMountDesc') is not None:
            self.secret_mount_desc = m.get('SecretMountDesc')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('ServiceTags') is not None:
            self.service_tags = m.get('ServiceTags')

        self.sidecar_containers_config = []
        if m.get('SidecarContainersConfig') is not None:
            for k1 in m.get('SidecarContainersConfig'):
                temp_model = main_models.SidecarContainerConfig()
                self.sidecar_containers_config.append(temp_model.from_map(k1))

        if m.get('SlsConfigs') is not None:
            self.sls_configs = m.get('SlsConfigs')

        if m.get('SlsLogEnvTags') is not None:
            self.sls_log_env_tags = m.get('SlsLogEnvTags')

        if m.get('StartupProbe') is not None:
            self.startup_probe = m.get('StartupProbe')

        if m.get('SwimlanePvtzDiscoverySvc') is not None:
            self.swimlane_pvtz_discovery_svc = m.get('SwimlanePvtzDiscoverySvc')

        if m.get('TerminationGracePeriodSeconds') is not None:
            self.termination_grace_period_seconds = m.get('TerminationGracePeriodSeconds')

        if m.get('Timezone') is not None:
            self.timezone = m.get('Timezone')

        if m.get('TomcatConfig') is not None:
            self.tomcat_config = m.get('TomcatConfig')

        if m.get('UpdateStrategy') is not None:
            self.update_strategy = m.get('UpdateStrategy')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('WarStartOptions') is not None:
            self.war_start_options = m.get('WarStartOptions')

        if m.get('WebContainer') is not None:
            self.web_container = m.get('WebContainer')

        return self

