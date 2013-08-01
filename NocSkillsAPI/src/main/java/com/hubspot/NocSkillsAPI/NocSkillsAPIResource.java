package com.hubspot.NocSkillsAPI;

import java.util.List;

import com.yammer.metrics.annotation.Timed;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

import com.mongodb.MongoClient;
import com.google.code.morphia.Datastore;
import com.google.code.morphia.Morphia;


@Path("/list")
@Produces(MediaType.APPLICATION_JSON)
public class NocSkillsAPIResource {
  private Datastore ds;
  
  public NocSkillsAPIResource(String mongoHost, int mongoPort, String mongoDBName) {
    try {
      MongoClient mongo = new MongoClient(mongoHost, mongoPort);
      Morphia morphia = new Morphia();
      morphia.map(Reason.class);
      this.ds = morphia.createDatastore(mongo, mongoDBName);
    } catch (Exception e) {
      System.out.println("Exception was caught trying to connect to mongo: " + e);
    }
  }
  
  @GET
  @Timed
  public List<Reason> getReasons() {
    return this.ds.find(Reason.class).asList();
  }
}
