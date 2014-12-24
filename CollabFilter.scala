import scala.collection.mutable.HashMap;

class CollabFilter() {
    val map = HashMap[String, HashMap[String, Double]]();

    def setRating(user: String, film: String, rating: Double) = map.apply(user).put(film, rating);

    def setUser(user: String) = map.put(user, new HashMap[String, Double]);

    def getRating(user: String, film: String) = map.apply(user).apply(film);

    def rate(user: String, film: String): Double = {
        val users = (for (i <- map.iterator if i._1 != user) yield i._1).toArray; //the set of users
        val filmsRated = map.apply(user).keySet; //the set of films rated by user U
        val films = users.iterator.zip(for (o <- users.iterator) yield (map.apply(o).keySet.intersect(filmsRated))).toArray;
        //films is an Iterator[(String, Set[String])] essentially, it iterates over the pairs (user O, set of shared films)
        //shared with user U by user O
        val top = for (o <- films.iterator) yield o._2.iterator.map((s: String) => map.apply(user).apply(s) * map.apply(o._1).apply(s)).sum;
        val left = for (o <- films.iterator) yield o._2.iterator.map((s: String) => map.apply(user).apply(s) * map.apply(user).apply(s).asInstanceOf[Double]).sum;
        val right = for (o <- films.iterator) yield o._2.iterator.map((s: String) => map.apply(o._1).apply(s) * map.apply(o._1).apply(s).asInstanceOf[Double]).sum;
        val bottom = left.zip(right);
        val sim = top.zip(bottom);
        val simils = users.iterator.zip(sim.map((s) => s._1 / (math.sqrt(s._2._1) * math.sqrt(s._2._2)))).toArray;
        val k = 1 / (for (s <- simils.iterator) yield s._2).sum;
        val weighted = simils.iterator.map((p) => p._2 * map.apply(p._1).apply(film)).sum;
        return weighted * k;
    }
}