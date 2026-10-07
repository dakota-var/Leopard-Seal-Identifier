package nz.co.dakotav.lepseal.model.observation;

@SuppressWarnings("SpellCheckingInspection")
public enum SourceSite {
    INATURALIST("iNaturalist", "https://www.inaturalist.nz/"),
    GBIF("GBIF", "https://www.gbif.org/");
    // More sites may be added here as needed

    // ============================================================================================

    private final String name;
    private final String url;

    SourceSite(String name, String url){
        this.name = name;
        this.url = url;
    }

    public String getName() {
        return name;
    }
    public String getUrl() {
        return url;
    }

    public static SourceSite fromName(String name) {
        for (SourceSite site : SourceSite.values()) {
            if (site.getName().equalsIgnoreCase(name)) {
                return site;
            }
        }
        throw new IllegalArgumentException("Invalid source site name: " + name);
    }

}
