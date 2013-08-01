package com.hubspot.NocSkillsAPI;

import com.yammer.dropwizard.Service;
import com.yammer.dropwizard.config.Bootstrap;
import com.yammer.dropwizard.config.Environment;

public class NocSkillsAPIService extends Service<NocSkillsAPIConfiguration> {

  /**
   * @param args
   */
  public static void main(String[] args) throws Exception {
    new NocSkillsAPIService().run(args);
  }

  @Override
  public void initialize(Bootstrap<NocSkillsAPIConfiguration> bootstrap) {
    bootstrap.setName("noc-skills");
    
  }

  @Override
  public void run(NocSkillsAPIConfiguration configuration, Environment environment) throws Exception {
    // TODO Auto-generated method stub
    final String mongoHost = configuration.getMongoHost();
    final int mongoPort = configuration.getMongoPort();
    final String mongoDBName = configuration.getMongoDBName();
    environment.addResource(new NocSkillsAPIResource(mongoHost, mongoPort, mongoDBName));
    environment.addHealthCheck(new NocSkillsAPIHealthCheck());
  }

}
